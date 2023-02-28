import graphene

import motorcycles.schema


class Query(motorcycles.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
