from animals import Animal, Dog, Bird, Fish, Cat


def main():
    # Create one instance of each animal subclass
    animals = []

    # TODO: instantiate your animals and add them to the list

    # Loop over all animals and call speak(), move(), and describe()
    for animal in animals:
        pass


if __name__ == "__main__":
    main()

from animals import Dog, Bird, Fish, Cat


dog = Dog("Buddy", 3, "Woof", "Golden Retriever")
bird = Bird("Tweety", 1, "Tweet", True)
fish = Fish("Nemo", 2, "Blub", "salt")
cat = Cat("Whiskers", 4, "Meow", True)


animals = [dog, bird, fish, cat]


for animal in animals:
    animal.speak()
    animal.move()
    animal.describe()
    print()