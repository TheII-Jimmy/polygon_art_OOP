import turtle
import random

class Shape:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-400, 400), random.randint(-300, 300)]
        self.color = self.get_new_color()
        self.border_size = random.randint(1, 10)

    def draw(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()

    def reduction(self, reduction_ratio):
        turtle.penup()
        turtle.forward(self.size * (1 - reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward(self.size * (1 - reduction_ratio) / 2)
        turtle.right(90)
        self.location[0], self.location[1] = turtle.pos()
        self.size *= reduction_ratio

    @staticmethod
    def get_new_color():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


class Triangle(Shape):
    def __init__(self):
        super().__init__(3)


class Square(Shape):
    def __init__(self):
        super().__init__(4)


class Pentagon(Shape):
    def __init__(self):
        super().__init__(5)


class ArtGenerator:
    def __init__(self):
        self.reduction_ratio = 0.618

    def setup(self):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)

    def generate(self, choice):
        self.setup()
        n_shape = random.randint(20, 40)
        method = getattr(self, f"pattern_{choice}")
        method(n_shape)
        turtle.update()

    def pattern_1(self, n):
        for _ in range(n):
            Triangle().draw()

    def pattern_2(self, n):
        for _ in range(n):
            Square().draw()

    def pattern_3(self, n):
        for _ in range(n):
            Pentagon().draw()

    def pattern_4(self, n):
        for _ in range(n):
            Shape(random.randint(3, 5)).draw()

    def pattern_5(self, n):
        for _ in range(n):
            obj = Triangle()
            for _ in range(3):
                obj.draw()
                obj.reduction(self.reduction_ratio)

    def pattern_6(self, n):
        for _ in range(n):
            obj = Square()
            for _ in range(3):
                obj.draw()
                obj.reduction(self.reduction_ratio)

    def pattern_7(self, n):
        for _ in range(n):
            obj = Pentagon()
            for _ in range(3):
                obj.draw()
                obj.reduction(self.reduction_ratio)

    def pattern_8(self, n):
        for _ in range(n):
            obj = Shape(random.randint(3, 5))
            for _ in range(3):
                obj.draw()
                obj.reduction(self.reduction_ratio)

    def pattern_9(self, n):
        for _ in range(n):
            obj = Shape(random.randint(3, 5))
            if random.random() > 0.5:
                for _ in range(3):
                    obj.draw()
                    obj.reduction(self.reduction_ratio)
            else:
                obj.draw()


if __name__ == "__main__":
    generator = ArtGenerator()
    choice = int(input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))
    generator.generate(choice)
    turtle.done()
