class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rec_perimeter(self):
        return (self.length + self.width)*2

    def rec_area(self):
        return self.length * self.width

    def display(self):
        print("The length of rectangle is: ", self.length)
        print("The width of rectangle is: ", self.width)
        print("The perimeter of rectangle is: ", self.rec_perimeter())
        print("The area of rectangle is: ", self.rec_area())


class Parallelepipede(Rectangle):
    def __init__(self, length, width , height):
        Rectangle.__init__(self, length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

newRec = Rectangle(12, 10)
print(newRec.rec_perimeter())
print(newRec.rec_area())
print(newRec.display())

myParallelepipede = Parallelepipede(7, 5, 2)
print("the volume of myParallelepipede is: " , myParallelepipede.volume())
