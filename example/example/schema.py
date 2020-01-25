import graphene
import graphql_jwt
import users.schema

class Query(users.schema.Query,
            graphene.ObjectType,):
    pass


class Mutation(# Insert other Mutations here
               graphene.ObjectType,):
    obtain_token = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)