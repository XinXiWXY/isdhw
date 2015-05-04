class Rectangle(object):
   def __init__(self, width, height):
        self.width = width
        self.height = height
        
   def area(self):
       return self.width * self.height

class Square(Rectangle):

   def __init__(self, width):
       self.width  = width
       self.height = width

class Ellipse(object):
    def __init__(self, halflongaxis, halfshortaxis):
        self.halflongaxis = halflongaxis
        self.halfshortaxis = halfshortaxis

    def area(self):
        return 3.14*  self.halflongaxis *  self.halfshortaxis
class Circle(Ellipse):

    def __init__(self,radius):
        self.halflongaxis = radius
        self.halfshortaxis = radius

def  compute__area
     return self.width * self.height + self.width * self.height
+ 3.14*  self.halflongaxis *  self.halfshortaxis +
3.14*  self.halflongaxis *  self.halfshortaxis



shapes = [Ellipse(10,20),Square(15),Ciecle(5),Rectangle(20,15)]

total__area = compute__area(shapes)
print (total__area)
