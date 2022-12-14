from abc import ABC, abstractmethod

class Rectangle(ABC):

    @abstractmethod
    def calculate(self):
        pass

class Rectangular(Rectangle):
    def __init__(self, width, length , depth):
        self.width = width
        self.length = length
        self.depth = depth

    def calculate(self): # override method
        return self.width * self.length * self.depth

if __name__ == "__main__":
    rect3D = Rectangular(8, 10, 5)
    print(f"ปริมาตรสี่เหลี่ยม ={rect3D.calculate()} ลบ.ม.")
