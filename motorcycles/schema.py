import graphene
from graphene_django import DjangoObjectType

from .models import Motocicleta


class MotocicletaType(DjangoObjectType):
    class Meta:
        model = Motocicleta


class Query(graphene.ObjectType):
    motorcycles = graphene.List(MotocicletaType)

    def resolve_motorcycles(self, info, **kwargs):
        return Motocicleta.objects.all()
