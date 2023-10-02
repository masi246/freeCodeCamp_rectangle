class Rectangle():
    '''In this project you will use object oriented programming to create a Rectangle class 
    and a Square class. The Square class should be a subclass of Rectangle and inherit methods 
    and attributes.'''
    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)
    def set_width(self, width):
        self._width = width
    def set_height(self, height):
        self._height = height
    def get_area(self):
        self._area = self._width * self._height
        return(self._area)
    def get_perimeter(self):
        self._perimeter = 2 * self._width + 2 * self._height
        return(self._perimeter)
    def get_diagonal(self):
        self._diagonal = (self._width ** 2 + self._height ** 2) ** .5
        return(self._diagonal)
    def get_picture(self):
        self._picture =  ""
        for h in range(self._height):
            self._picture = "*"*self._width + "\n" + self._picture
        return(self._picture)
    def __str__(self):
        return(f"Rectangle(width={self._width}, height={self._height})")
    def get_amount_inside(self, shape):
        return self.get_area() //shape.get_area()
class Square(Rectangle):
    def __init__(self,  side_length):
        self._width = side_length
        self._height = side_length
    def set_side(self, side_length):
        self._width = side_length
        self._height = side_length
    def __str__(self):
        return (f"Square(side={self._width})")