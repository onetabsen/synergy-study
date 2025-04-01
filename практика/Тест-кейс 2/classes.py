class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return "Some generic sound"
    
    def move(self):
        return f"{self.name} is moving"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    
    def fetch(self, item):
        return f"{self.name} is fetching the {item}"

class Bird(Animal):
    def make_sound(self):
        return "Chirp!"
    
    def fly(self):
        return f"{self.name} is flying"

# Тестовая программа
def test_animal_classes():
    # Создаем экземпляры классов
    generic_animal = Animal("Generic Animal")
    dog = Dog("Rex")
    bird = Bird("Tweety")

    # Демонстрация методов базового класса
    print("=== Base class methods ===")
    print(generic_animal.make_sound())  # Some generic sound
    print(generic_animal.move())       # Generic Animal is moving

    # Демонстрация методов производного класса Dog
    print("\n=== Dog class methods ===")
    print(dog.make_sound())            # Woof!
    print(dog.move())                  # Rex is moving
    print(dog.fetch("ball"))           # Rex is fetching the ball

    # Демонстрация методов производного класса Bird
    print("\n=== Bird class methods ===")
    print(bird.make_sound())           # Chirp!
    print(bird.move())                 # Tweety is moving
    print(bird.fly())                  # Tweety is flying

    # Проверка наследования
    print("\n=== Inheritance check ===")
    print(isinstance(dog, Animal))     # True
    print(isinstance(bird, Animal))    # True
    print(issubclass(Dog, Animal))     # True
    print(issubclass(Bird, Animal))    # True

if __name__ == "__main__":
    test_animal_classes()