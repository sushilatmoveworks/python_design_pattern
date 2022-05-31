import random
from typing import Type

class Pet:
    def __init__(self, name: str) -> None:
        self._name = name

    def speak(self) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class Dog(Pet):
    def speak(self):
        print('woof')

    def __str__(self) -> str:
        return f'Dog {self._name}'

class Cat(Pet):
    def speak(self):
        print('meow')

    def __str__(self) -> str:
        return f'Cat {self._name}'

class Petshop:
    def __init__(self, pet_factory: Type[Pet]) -> None:
        self._pet_factory = pet_factory

    def buy_pet(self, name: str) -> Pet:
        pet = self._pet_factory(name)
        print(f'pet bought {pet}')
        return pet

def random_animal(name: str) -> Pet:
    return random.choice([Dog, Cat])(name)

def main() -> None:
    """
    >>> cat_shop = Petshop(Cat)
    >>> pet = cat_shop.buy_pet("lucy")
    pet bought Cat lucy
    >>> pet.speak()
    meow

    >>> pet_shop = Petshop(random_animal)
    >>> for name in ["Max", "Jack", "Buddy"]:
    ...     pet = pet_shop.buy_pet(name)
    ...     pet.speak()
    pet bought Cat Max
    meow
    pet bought Dog Jack
    woof
    pet bought Dog Buddy
    woof
    """

if __name__=='__main__':
    random.seed(1234)
    import doctest

    doctest.testmod()
