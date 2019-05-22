class Point:
    def move(self):
        print("move")


    def draw(self):
         print("draw")


#object creation in python
point1 = Point()
#Attributes for the object can be set anywhere in the program
point1.x=10
point1.y=20
print(point1.x)
point1.draw()
