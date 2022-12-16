from abc import ABC, abstractmethod
class Geomentry(ABC):
    def __init__(self, base, height):
        self.base = base
        self.height = height

        @abstractmethod
        def calArea(self):
            #คำนวณหาพื้นที่
            pass

#พื้นที่สามเหลี่ยม
class Triangle(Geomentry):
    def __init__(self, base, height):
        super().__init__(base, height)

    def calArea(self):
        return 0.5 * self.base * self.height

#พื้นที่สี่เหลี่ยมด้านขนาน
class Parallel(Geomentry):
    def __init__(self, base, height):
        super().__init__(base, height)

    def calArea(self):
        return self.base * self.height

#พื้นที่รูปขนมเปียกปูน
class Rhombus(Geomentry):
    def __init__(self, base, height):
        super().__init__(base, height)

    def calArea(self):
        return self.base * self.height

if __name__ == "__main__":
    triangle = Triangle(10,6)
    print(f"พื้นที่สามเหลี่ยม = {triangle.calArea()} ตร.ม.")

    parallel = Parallel(10,6)
    print(f"พื้นที่สี่เหลี่ยมด้านขนาน = {parallel.calArea()} ตร.ม.")

    rhombus = Rhombus(10,6)
    print(f"พื้นที่รูปขนมเปียกปูน = {rhombus.calArea()} ตร.ม.")
