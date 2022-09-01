class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self,height):
        self.height = height

    def get_area(self):
        return (self.width * self.height)

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((width ** 2 + height ** 2) ** .5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return ("Too big for picture.")
        firstline = "*"*self.width + "\n"
        picture = firstline * self.height
        return picture

    # def get_amount_inside(self, instance):




# class Square:

rectangle = Rectangle(10, 5)
print(rectangle.get_picture())
