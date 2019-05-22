class Point:
    #defininng the constuctor via init method
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
print(point.x)



class Person:
    def __init__(self,name):
        self.name=name

    def talk(self):
        print(f'{self.name} is talking')

#create object
person=Person("Vikas")
person.talk()