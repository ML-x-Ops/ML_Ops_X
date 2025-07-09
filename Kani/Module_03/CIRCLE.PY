class Circle:
    def draw_circle(self, radius):
        print(f"Drawing circle with radius {radius}")

class Triangle:
    def draw_triangle(self, base, height):
        print(f"Drawing triangle with base {base} and height {height}")

class Adapter_Circle:
    def __init__(self,area_circle):
        self.area_circle = area_circle

    def draw(self,radius):
        self.area_circle.draw_circle(radius)

class Adapter_Triangle:
    def __init__(self,area_triangle):
        self.area_triangle = area_triangle

    def draw(self,base,height):
        self.area_triangle.draw_triangle(base,height)


cir = Circle()

tri = Triangle()

a_cir = Adapter_Circle(cir)

a_tri = Adapter_Triangle(tri)

a_cir.draw(45)

a_tri.draw(5,4)
