class Shape:
    def __init__(self, name):
        self.name = name
        self.area = None
        self.perimeter = None

    def display(self):
        print(f'{self.name} has an area of {self.area} and perimeter of {self.perimeter}')

class Square(Shape):

    def __init__(self, side):
        self.side = side
        super().__init__('Square')
        self.area=self.compute_area()
        self.perimeter=self.compute_perimeter()

    def compute_area(self):
        self.area = self.side * self.side
        return self.area
    
    def compute_perimeter(self):
        self.perimeter = 4 * self.side
        return self.perimeter

print(Square(4))
#print(Square(5).compute_area())
#print(Square(5).compute_perimeter())