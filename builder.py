class Building:
    def __init__(self):
        self.build_floor()
        self.build_size()

    def build_floor(self):
        raise NotImplementedError

    def build_size(self):
        raise NotImplementedError

    def __repr__(self):
        return f'floor: {self.floor} | size: {self.size}'

class House(Building):
    def build_floor(self):
        self.floor = 'One'

    def build_size(self):
        self.size = 'Large'

class Apartment(Building):
    def build_floor(self):
        self.floor = 'Two'

    def build_size(self):
        self.size = 'Small'

def main():
    """
    >>> house = House()
    >>> house
    floor: One | size: Large

    >>> apartment = Apartment()
    >>> apartment
    floor: Two | size: Small
    """

if __name__=='__main__':
    import doctest
    doctest.testmod()
