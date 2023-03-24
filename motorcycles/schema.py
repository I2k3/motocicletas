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
        motocicleta = Motocicleta(marca=marca, modelo=modelo, motor=motor, consumog=consumog, capacidadg=capacidadg, cilindraje=cilindraje, version=version, color=color, precio=precio, description=description)
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
        )


class Mutation(graphene.ObjectType):
    create_motocicleta = CreateMotocicleta.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
