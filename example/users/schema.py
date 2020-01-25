from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class Query(graphene.ObjectType):
    current_user = graphene.Field(UserType)

    def resolve_current_user(self, info, **kwargs):
        user = info.context.user

        return user
