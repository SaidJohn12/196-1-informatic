from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @abstractmethod
    def sound(self):
        ...

    @abstractmethod
    def food_per_day(self):
        ...

    def describe(self):
        return self.name + ": " + self.sound()


class Lion(Animal):
    def sound(self):
        return "Р-р-р"

    def food_per_day(self):
        return self.weight * 0.05


class Parrot(Animal):
    def sound(self):
        return "Привет!"

    def food_per_day(self):
        return self.weight * 0.10


class Zoo:
    def __init__(self):
        self.animals = []

    def add(self, animal):
        if not isinstance(animal, Animal):
            raise TypeError("В зоопарк можно добавлять только животных!")
        self.animals.append(animal)

    def sounds(self):
        result = []
        for a in self.animals:
            result.append(a.describe())
        return result

    def total_food(self):
        total = 0
        for a in self.animals:
            total = total + a.food_per_day()
        return total

    def __len__(self):
        return len(self.animals)