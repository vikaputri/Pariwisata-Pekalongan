import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene.types import Scalar
import django_filters
from graphene_django import DjangoObjectType
from .models import Article, Category, Oleholeh, Kuliner
from django.db.models import Q

class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = ("id", "name", "slug", "article")

class  CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        interfaces = (graphene.relay.Node , )

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "slug", "article")

class FileField(Scalar):
    @staticmethod
    def serialize(value):
        if not value:
            return ""
        return value.url

    @staticmethod
    def parse_literal(node):
        return node

    @staticmethod
    def parse_value(value):
        return value

class ArticleType(DjangoObjectType):
    image = FileField()
    class Meta:
        model = Article
        fields = ("id", "title", "content", "alamat", "telepon","jam", 
            "harga", "slug", "image", "Category", "date_created", "date_modified")
        filter_fields = ["image"]

class ArticleFilter(django_filters.FilterSet):
    class Meta:
        model = Article
        exclude = ['image']
        fields = ("title", "content", "alamat", "telepon","jam", 
            "harga", "slug", "Category", "date_created", "date_modified")

class ArticleNode(DjangoObjectType):
    image = FileField()
    class Meta:
        model = Article
        interfaces = (graphene.relay.Node , )

class OleholehType(DjangoObjectType):
    image = FileField()
    class Meta:
        model = Oleholeh
        fields = ("id", "title", "description", "slug", "content", "image")
        filter_fields = ["image"]

class OleholehFilter(django_filters.FilterSet):
    class Meta:
        model = Oleholeh
        exclude = ['image']
        fields = ("title", "description", "slug", "content")

class OleholehNode(DjangoObjectType):
    image = FileField()
    class Meta:
        model = Oleholeh
        interfaces = (graphene.relay.Node , )

class KulinerType(DjangoObjectType):
    image = FileField()
    class Meta:
        model = Kuliner
        fields = ("id", "title", "description", "slug", "content", "image")
        filter_fields = ["image"]

class KulinerFilter(django_filters.FilterSet):
    class Meta:
        model = Kuliner
        exclude = ['image']
        fields = ("title", "description", "slug", "content")

class KulinerNode(DjangoObjectType):
    image = FileField()
    class Meta:
        model = Kuliner
        interfaces = (graphene.relay.Node , )

class Query(graphene.ObjectType):
    category = graphene.List(CategoryType)
    node = graphene.relay.Node.Field()
    articles =  DjangoFilterConnectionField(ArticleNode,
        filterset_class=ArticleFilter, name=graphene.String())
    article = graphene.Field(ArticleType, slug=graphene.String(required=True))
    categories = graphene.Field(CategoryType, slug=graphene.String(required=True))
    oleholehs =  DjangoFilterConnectionField(OleholehNode,
        filterset_class=OleholehFilter, name=graphene.String())
    oleholeh = graphene.Field(OleholehType, slug=graphene.String(required=True))
    kuliners =  DjangoFilterConnectionField(KulinerNode,
        filterset_class=KulinerFilter, name=graphene.String())
    kuliner = graphene.Field(KulinerType, slug=graphene.String(required=True))

    def resolve_articles(self, info, name=None,category_id=None, **kwargs):
        if name:
            filter = (
                Q(title__icontains=name) |
                Q(description__icontains=name)
            )
            return Article.objects.filter(filter)

        return Article.objects.all()

    def resolve_category(root, info):
        return Category.objects.all()

    def resolve_article(root, info, slug):
        try:
            return Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            return None

    def resolve_categories(root, info, slug):
        try:
            return Category.objects.get(slug=slug)
        except Category.DoesNotExist:
            return None
    
    def resolve_image(self, info, id):
        return Article.objects.get(id=id)

    def resolve_oleholeh(root, info, slug):
        try:
            return Oleholeh.objects.get(slug=slug)
        except Oleholeh.DoesNotExist:
            return None

    def resolve_kuliner(root, info, slug):
        try:
            return Kuliner.objects.get(slug=slug)
        except Kuliner.DoesNotExist:
            return None 
    

class Image(graphene.Mutation):
    image = graphene.Field(ArticleType)
    @classmethod
    def mutate(cls, root, info):
        files = info.context.FILES['imageFile']
        imgobj = Article(image=files)
        imgobj.save()
        return Image(profile_image=imgobj)

class Mutation(graphene.ObjectType):
    image = Image.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
            
#schema = graphene.Schema(query=Query)