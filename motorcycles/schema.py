import graphene
from graphene_django import DjangoObjectType
from users.schema import UserType
from .models import Motocicleta
from motorcycles.models import Motocicleta, Vote
from graphql import GraphQLError
from django.db.models import Q





class MotocicletaType(DjangoObjectType):
    class Meta:
        model = Motocicleta
# ...code
# Add after the LinkType
class VoteType(DjangoObjectType):
    class Meta:
        model = Vote


class Query(graphene.ObjectType):
    motorcycles = graphene.List(MotocicletaType, search=graphene.String())
    votes = graphene.List(VoteType)


    def resolve_motorcycles(self, info, search=None, **kwargs):
        # The value sent with the search parameter will be in the args variable
        if search:
            filter = (
                Q(description__icontains=search)|
                Q(marca__icontains=search)

            )
            return Motocicleta.objects.filter(filter)

        return Motocicleta.objects.all()

        
    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()

class CreateMotocicleta(graphene.Mutation):
    id = graphene.Int()
    marca = graphene.String()
    modelo = graphene.String()
    motor = graphene.String()
    consumog = graphene.Int()
    capacidadg = graphene.Float()
    cilindraje = graphene.Int()
    version = graphene.String()
    color = graphene.String()
    precio = graphene.Decimal()
    description = graphene.String()
    posted_by = graphene.Field(UserType)




    class Arguments:
        
        marca = graphene.String()
        modelo = graphene.String()
        motor = graphene.String()
        consumog = graphene.Int()
        capacidadg = graphene.Float()
        cilindraje = graphene.Int()
        version = graphene.String()
        color = graphene.String()
        precio = graphene.Decimal()
        description = graphene.String()
        


    def mutate(self, info, marca, modelo, motor, consumog, capacidadg, cilindraje, version, color, precio, description):
        user = info.context.user or None

        motocicleta = Motocicleta(marca=marca, modelo=modelo, motor=motor, consumog=consumog, capacidadg=capacidadg, cilindraje=cilindraje, version=version, color=color, precio=precio, description=description,posted_by=user,)
        motocicleta.save()

        return CreateMotocicleta(
            id=motocicleta.id,
            marca=motocicleta.marca,
            modelo=motocicleta.modelo,
            motor=motocicleta.motor,
            consumog=motocicleta.consumog,
            capacidadg=motocicleta.capacidadg,
            cilindraje=motocicleta.cilindraje,
            version=motocicleta.version,
            color=motocicleta.color,
            precio=motocicleta.precio,
            description=motocicleta.description,
            posted_by=motocicleta.posted_by,

        )

class CreateVote(graphene.Mutation):
    user = graphene.Field(UserType)
    motocicleta = graphene.Field(MotocicletaType)

    class Arguments:
        motocicleta_id = graphene.Int()

    def mutate(self, info, motocicleta_id):
        user = info.context.user
        if user.is_anonymous:
 #1
            raise GraphQLError('You must be logged to vote!')
        motocicleta = Motocicleta.objects.filter(id=motocicleta_id).first()
        if not motocicleta:
 #2
            raise Exception('Invalid Link!')

        Vote.objects.create(
            user=user,
            motocicleta=motocicleta,
        )

        return CreateVote(user=user, motocicleta=motocicleta)


class Mutation(graphene.ObjectType):
    create_motocicleta = CreateMotocicleta.Field()
    create_motocicleta = CreateMotocicleta.Field()
    create_vote = CreateVote.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
