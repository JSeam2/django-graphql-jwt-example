from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

    # Be sure to exclude sensitive data here
    # exclude_fields = (
    #     'password',
    #     'email',
    #     'paypal_email',
    #     'is_superuser',
    # )


class Query(graphene.ObjectType):
    current_user = graphene.Field(UserType)

    def resolve_current_user(self, info, **kwargs):
        user = info.context.user

        return user


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username=username,
            email=email,
        )

        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class Mutation(graphene.AbstractType):
    create_user = CreateUser.Field()
