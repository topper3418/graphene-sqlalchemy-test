import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from .models import Person, Pet, Location, Belonging
from ..db import (Person as PersonModel,
                  Pet as PetModel,
                  Location as LocationModel,
                  Belonging as BelongingModel)
from ..db import db_session as db




class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_people = SQLAlchemyConnectionField(Person.connection)
    all_pets = SQLAlchemyConnectionField(Pet.connection)
    all_locations = SQLAlchemyConnectionField(Location.connection)
    all_belongings = SQLAlchemyConnectionField(Belonging.connection)

class CreatePerson(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        age = graphene.Int(required=True)

    person = graphene.Field(Person)

    def mutate(self, info, name):
        person = PersonModel(name=name)
        db.session.add(person)
        db.session.commit()
        return CreatePerson(person=person)

class UpdatePerson(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()

    person = graphene.Field(Person)

    def mutate(self, info, id, name=None):
        person = PersonModel.query.filter_by(id=id).first()
        if name:
            person.name = name
        db.session.commit()
        return UpdatePerson(person=person)

class DeletePerson(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    person = graphene.Field(Person)

    def mutate(self, info, id):
        person = PersonModel.query.filter_by(id=id).first()
        db.session.delete(person)
        db.session.commit()
        return DeletePerson(person=person)

class CreatePet(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        favorite_person_id = graphene.ID(required=True)

    pet = graphene.Field(Pet)

    def mutate(self, info, name, favorite_person_id):
        pet = PetModel(name=name, favorite_person_id=favorite_person_id)
        db.session.add(pet)
        db.session.commit()
        return CreatePet(pet=pet)

class UpdatePet(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        favorite_person_id = graphene.ID()

    pet = graphene.Field(Pet)

    def mutate(self, info, id, name=None, favorite_person_id=None):
        pet = PetModel.query.filter_by(id=id).first()
        if name:
            pet.name = name
        if favorite_person_id:
            pet.favorite_person_id = favorite_person_id
        db.session.commit()
        return UpdatePet(pet=pet)

class DeletePet(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    pet = graphene.Field(Pet)

    def mutate(self, info, id):
        pet = PetModel.query.filter_by(id=id).first()
        db.session.delete(pet)
        db.session.commit()
        return DeletePet(pet=pet)
    
class CreateLocation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    location = graphene.Field(Location)

    def mutate(self, info, name):
        location = LocationModel(name=name)
        db.session.add(location)
        db.session.commit()
        return CreateLocation(location=location)

class UpdateLocation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()

    location = graphene.Field(Location)

    def mutate(self, info, id, name=None):
        location = LocationModel.query.filter_by(id=id).first()
        if name:
            location.name = name
        db.session.commit()
        return UpdateLocation(location=location)
    
class DeleteLocation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    location = graphene.Field(Location)

    def mutate(self, info, id):
        location = LocationModel.query.filter_by(id=id).first()
        db.session.delete(location)
        db.session.commit()
        return DeleteLocation(location=location)

class CreateBelonging(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        favorite_person_id = graphene.ID(required=True)
        pet_id = graphene.ID(required=True)

    belonging = graphene.Field(Belonging)

    def mutate(self, info, name, favorite_person_id, pet_id):
        belonging = BelongingModel(name=name, favorite_person_id=favorite_person_id, pet_id=pet_id)
        db.session.add(belonging)
        db.session.commit()
        return CreateBelonging(belonging=belonging)

class UpdateBelonging(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        favorite_person_id = graphene.ID()
        pet_id = graphene.ID()

    belonging = graphene.Field(Belonging)

    def mutate(self, info, id, name=None, favorite_person_id=None, pet_id=None):
        belonging = BelongingModel.query.filter_by(id=id).first()
        if name:
            belonging.name = name
        if favorite_person_id:
            belonging.favorite_person_id = favorite_person_id
        if pet_id:
            belonging.pet_id = pet_id
        db.session.commit()
        return UpdateBelonging(belonging=belonging)

class DeleteBelonging(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    belonging = graphene.Field(Belonging)

    def mutate(self, info, id):
        belonging = BelongingModel.query.filter_by(id=id).first()
        db.session.delete(belonging)
        db.session.commit()
        return DeleteBelonging(belonging=belonging)

class Mutation(graphene.ObjectType):
    create_person = CreatePerson.Field()
    update_person = UpdatePerson.Field()
    delete_person = DeletePerson.Field()
    create_pet = CreatePet.Field()
    update_pet = UpdatePet.Field()
    delete_pet = DeletePet.Field()
    create_location = CreateLocation.Field()
    update_location = UpdateLocation.Field()
    delete_location = DeleteLocation.Field()
    create_belonging = CreateBelonging.Field()
    update_belonging = UpdateBelonging.Field()
    delete_belonging = DeleteBelonging.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)