class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self): 
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self,height):
        self.height = height

    def get_area(self):
        area = (self.width * self.height)
        return area

    def get_perimeter(self):
        perimeter = (2 * self.width + 2 * self.height)
        return perimeter

    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return ("Too big for picture.")
        firstline = "*"*self.width + "\n"
        picture = firstline * self.height
        return picture

    def get_amount_inside(self, instance):
        amount = int((self.width / instance.width) * (self.height / instance.height))
        return amount




class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        self.width = self.side
        self.height = self.side
        Rectangle.__init__(self, self.width, self.height)

    def set_side(self, side):
        self.side = side
        Rectangle.set_width(self, side)
        Rectangle.set_height(self, side)

    def __repr__(self): 
        self.side = self.width
        return f"Square(side={self.side})"




# rectangle = Rectangle(10, 5)
# square = Square(5)
# square.set_side(2)
# square.set_side(4)
# print(rectangle.get_picture())
# print(rectangle.get_amount_inside(square))
# print(square.get_picture())
