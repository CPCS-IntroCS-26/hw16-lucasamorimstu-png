class Animal:
    def __init__(self, name, age, sound):
        pass

    def speak(self):
        pass

    def move(self):
        pass

    def describe(self):
        pass

    def __str__(self):
        pass


class Dog(Animal):
    def __init__(self, name, age, breed):
        pass

    def speak(self):
        pass

    def move(self):
        pass


class Bird(Animal):
    def __init__(self, name, age, can_fly):
        pass

    def move(self):
        pass


class Fish(Animal):
    def __init__(self, name, age, water_type):
        pass

    def move(self):
        pass


class Cat(Animal):
    def __init__(self, name, age, indoor):
        pass

    def speak(self):
        pass

    def move(self):
        pass

class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def speak(self):
        print(f"{self.name} says {self.sound}")

    def move(self):
        print(f"{self.name} moves in a generic way.")

    def describe(self):
        print(f"{self.name} is a {self.age}-year-old {self.__class__.__name__}.")

    def __str__(self):
        return f"{self.name} ({self.__class__.__name__})"


# ----------------- DOG -----------------
class Dog(Animal):
    def __init__(self, name, age, sound, breed):
        super().__init__(name, age, sound)
        self.breed = breed

    def speak(self):
        print(f"{self.name} barks: {self.sound}!")

    def move(self):
        print(f"{self.name} runs on four legs.")

# ----------------- BIRD -----------------
class Bird(Animal):
    def __init__(self, name, age, sound, can_fly=True):
        super().__init__(name, age, sound)
        self.can_fly = can_fly

    def move(self):
        if self.can_fly:
            print(f"{self.name} flies through the air.")
        else:
            print(f"{self.name} walks on the ground.")

# ----------------- FISH -----------------
class Fish(Animal):
    def __init__(self, name, age, sound, water_type):
        super().__init__(name, age, sound)
        self.water_type = water_type

    def move(self):
        print(f"{self.name} swims in {self.water_type} water.")

# ----------------- CAT -----------------
class Cat(Animal):
    def __init__(self, name, age, sound, indoor):
        super().__init__(name, age, sound)
        self.indoor = indoor

    def speak(self):
        print(f"{self.name} meows softly: {self.sound}")

    def move(self):
        if self.indoor:
            print(f"{self.name} walks around the house.")
        else:
            print(f"{self.name} explores outside stealthily.")