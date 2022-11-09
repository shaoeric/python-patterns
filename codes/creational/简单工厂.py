# Product
class Shape:
    def draw(self):
        raise NotImplementedError


class Circle(Shape):
    def draw(self):
        print("绘制圆形")


class Rectangle(Shape):
    def draw(self):
        print("绘制矩形")


# Factory
class ShapeFactory:
    def create(self, shape_name):
        if shape_name == '圆形':
            return Circle()
        elif shape_name == '矩形':
            return Rectangle()
        else:
            raise TypeError
    

if __name__ == '__main__':
    factory = ShapeFactory()
    obj = factory.create('圆形')
    obj.draw()