class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("子类必须实现speak()")
    
class Dog(Animal):
    def speak(self):
        return "woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow"
    
animals = [
    Dog("大黄"),
    Cat("咪咪"),
    Dog("小黑"),
    Cat("咖啡")
]

for animal in animals:
    print(f"{animal.name}的叫声： {animal.speak()}")