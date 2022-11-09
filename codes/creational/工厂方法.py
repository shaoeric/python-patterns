from abc import ABCMeta, abstractmethod

# Product
class Shape(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("绘制圆形")

class Rectangle(Shape):
    def draw(self):
        print("绘制矩形")


# Factory
class ShapeFactory(metaclass=ABCMeta):
    @abstractmethod
    def create(self):
        pass

class CircleFactory(ShapeFactory):
    def create(self):
        return Circle()
    
class RectangleFactory(ShapeFactory):
    def create(self):
        return Rectangle()
    

if __name__ == '__main__':
    factory = CircleFactory()
    obj = factory.create()
    obj.draw()