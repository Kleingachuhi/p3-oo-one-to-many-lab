
class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self, name, pet_type, owner = "John"):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Pet must be among the pet types in PET_TYPES")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
class Owner:
    def __init__(self,name):
        self.name = name
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Can only add instances of Pet")
        pet.owner = self
        


    def get_sorted_pets(self):
            return sorted(self.pets(), key=lambda pet: pet.name)



owner = Owner("Ben")
pet1 = Pet("Fido", "dog", owner)
pet2 = Pet("Clifford", "dog", owner )
pet3 = Pet("Whiskers", "cat", owner )
pet4 = Pet("Jerry", "reptile", owner)

pet5 = Pet("Lucky", "dog")
owner.add_pet(pet5)
