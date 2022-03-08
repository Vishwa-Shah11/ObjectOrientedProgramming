class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.valid = False

        if ((self.a + self.b <= self.c) or (self.b + self.c <= self.a) or (self.c + self.a <= self.b)):
            self.valid = False
        else:
            self.valid = True
        
    def is_equilateral(self):
        if (self.valid):
            if (self.a == self.b == self.c):
                return True
            return False
        
    def is_isosceles(self):
        if (self.valid):
            if ((self.a == self.b or self.b == self.c or self.c == self.a) and (not self.is_equilateral())):
                return True
            return False
        
    def is_scalene(self):
        if (self.valid):
            if (self.a != self.b and self.b != self.c and self.c != self.a):
                return True
            return False

obj = Triangle(1,2,3)
print(obj.is_equilateral())
print(obj.is_isosceles())
print(obj.is_scalene())