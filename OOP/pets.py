class Pet:
    allowed = ['cat', 'dog', 'fish', 'rat']
    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} animal.")
        self.name = name
        self.species = species
    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} animal.")
        self.species = species

cat = Pet("Jimmy", "cat")
dog = Pet("Wyatt", "dog")
tiger = Pet("Fluffy", "Tiger") 