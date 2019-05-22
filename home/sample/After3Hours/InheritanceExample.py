class Mammal:
    def walk(self):
        print("Walk")

#Dog class inherits all the methods of mammal class
class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def meaw(self):
        print("Meaw")

#createing objec
dog1= Dog()
dog1.bark()
dog1.walk()

cat1= Cat()
cat1.meaw()
Cat().meaw()

