import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from ..db import (Person as PersonModel,
                  Pet as PetModel,
                  Location as LocationModel,
                  Belonging as BelongingModel)


class Person(SQLAlchemyObjectType):
    class Meta:
        model = PersonModel
        interfaces = (relay.Node, )


class Pet(SQLAlchemyObjectType):
    class Meta:
        model = PetModel
        interfaces = (relay.Node, )


class Location(SQLAlchemyObjectType):
    class Meta:
        model = LocationModel
        interfaces = (relay.Node, )


class Belonging(SQLAlchemyObjectType):
    class Meta:
        model = BelongingModel
        interfaces = (relay.Node, )