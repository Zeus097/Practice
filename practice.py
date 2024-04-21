class Zoo:
    __animals = 0

    def __init__(self, current_zoo_name):
        self.name = current_zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        string = ""
        if species == 'mammal':
            string += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == 'fish':
            string += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == 'bird':
            string += f"Birds in {self.name}: {', '.join(self.birds)}\n"

        string += f"Total animals: {Zoo.__animals}"
        return string


zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())
for i in range(count):
    animals = input().split()
    current_species = animals[0]
    current_name = animals[1]
    if current_species == 'mammal':
        zoo.add_animal(current_species, current_name)
    elif current_species == 'fish':
        zoo.add_animal(current_species, current_name)
    elif current_species == 'bird':
        zoo.add_animal(current_species, current_name)

species_info = input()
print(zoo.get_info(species_info))
