# oopbasic.py

class student:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def study(self):
        print(f"{self.name}กำลังเรียนอยู่...")

    def sawatdee(self):
        if self.gender == "ชาย":
            tail = "ครับ"
            callme = "ผม"
        else:
            tail = "ค่ะ"
            callme = "หนู"
        print(f"สวัสดี{tail}{callme}ชื่อ{self.name}")


class specialstudent(student):

    def __init__(self, name, age, gender,parent):
        super().__init__(name, age, gender)
        self.parent = parent

    def hello(self, person="เพื่อน"):
        if person == "เพื่อน":
            print("เฮ้ย ว่าไงมีขนมกินไหม?")
        else:
            print("รีบเดินหนีดีกว่า")

    def sawatdee(self):
        print(f"ว่าไง ชื่อ{self.name}")
    
    def myfather(self):
        print("รู้ไหมผมลูกใคร")
        print(f"ผมลูก{self.parent}")


class teacher :
    def __init__(self,name,gender,subject):
        self.name = name
        self.gender = gender
        self.subject = subject

    def teach(self):
        print("คุณครู{}กำลังสอนวิชา{}".format(self.name,self.subject))


if __name__ == "__main__" :
    student1 = student("ป้อม",14,"ชาย")
    student2 = student("สมศรี",14,"หญิง")
    special_student = specialstudent("จ้อย",16,"ชาย","นายก อบต.เจท")

    teacher1 = teacher("จอร์น","ชาย","ภาษาอังกฤษ")
    print(teacher1.name)
    print(teacher1.subject)

    print("------8.30 น.------")
    student1.sawatdee()
    student2.sawatdee()
    teacher1.teach()
    student1.study()
    student2.study()
    print("------8.45 น.------")
    special_student.sawatdee()
    special_student.hello("ครู")
    print("เดินไปที่โต๊ะตัวเอง")
    special_student.hello("เพื่อน")
    print(f"ครู{teacher1.name}! ขอเกรดดีๆหน่อย")
    special_student.myfather()

