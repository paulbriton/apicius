import graphene
from apicius import queries

schema = graphene.Schema(query=queries.Query)
