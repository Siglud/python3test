# coding=utf-8
__author__ = 'Siglud'
#简单工厂


class Shape(object):
    """绘制图形"""
    def draw(self):
        raise SyntaxError

    def erase(self):
        raise SyntaxError


class Circle(Shape):
    """圆形"""
    def __init__(self, radius=0):
        self.__radius = radius

    def draw(self):
        print "Draw a circle"

    def erase(self):
        print("erase circle")

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius


class Rectangle(Shape):
    """矩形"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def draw(self):
        print("Draw Rectangle")

    def erase(self):
        print("erase Rectangle")

    def getWidth(self):
        return self.__width

    def setWidth(self, width):
        self.__width = width

    def getHeight(self):
        return self.__height

    def setHeight(self, height):
        self.__height = height


class ShapeFactory(object):
    def factory(self, which):
        if which == "Circle":
            return Circle()
        elif which == "Rectangle":
            return Rectangle()
        else:
            return None

if __name__ == "__main__":
    fac = ShapeFactory()
    shape = fac.factory("Circle")
    if shape is not None:
        shape.draw()