import graphene
from graphene_django import DjangoObjectType
import graphql_jwt
import users.schema

from django.contrib.auth import get_user_model

class Query(users.schema.Query,
            graphene.ObjectType,):
    pass


class Mutation(users.schema.Mutation,
               graphene.ObjectType,):
    obtain_token = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
