import graphene

import motorcycles.schema


class Query(motorcycles.schema.Query, graphene.ObjectType):
    pass

class Mutation(motorcycles.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
schema = graphene.Schema(query=Query, mutation=Mutation)