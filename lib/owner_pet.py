class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = [] 

    def pets(self):
        """Returns a full list of the owner's pets."""
        return self._pets

    def add_pet(self, pet):
        """Checks if the pet is of type Pet and adds the owner to the pet."""
        if not isinstance(pet, Pet):
            raise Exception(f"{pet} is not a valid Pet instance.")
        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        """Returns a sorted list of pets by their names."""
        return sorted(self._pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}.")

        if owner is not None and not isinstance(owner, Owner):
            raise Exception(f"{owner} is not a valid Owner instance.")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self) 

        
        if owner:
            owner.add_pet(self)

