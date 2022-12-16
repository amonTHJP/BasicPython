class BankAccount:

    def __init__(self, name, age, amount):
        self.name = name
        self._age = age #protected
        self.__amount = amount #private

    def showMessage(self):
        print("กำลังทำรายการฝากถอนในบัญชี")

    def _deposit(self, deposit):
        self.__amount += deposit
        print(f"ฝากเพิ่ม {deposit} รวมเงิน {self.__amount}")

#ใช้ private วิธีแรก
    # def getAmount(self):     #Getter
    #     return self.__amount

    # def setAmount(self, amount):    #Setter
    #     self.__amount = amount

#ใช้ private วิธีที่สอง
    @property
    def amounts(self):     #Getter
        return self.__amount

    @amounts.setter
    def amounts(self, amount):    #Setter
        self.__amount = amount

    def withdraw(self, withdraw):
        self.__amount -= withdraw
        print(f"ถอนออก {withdraw} เหลือเงิน {self.__amount}")

    # data = property(getAmount, setAmount) #ใช้ private วิธีแรก

    
class Employee(BankAccount):
    def __init__(self, name, age, amount):
        super().__init__(name, age, amount)


if __name__ == "__main__":
    employee = Employee("สมชาย รวยมาก", 20, 100000)
    print(employee.name)
    print(f"อายุ {employee._age} ปี")
    
    # #ใช้ private วิธีแรก
    # print(employee.data)
    # employee.data = 200000
    # print(employee.data)

    #ใช้ private วิธีที่สอง
    print(employee.amounts)
    employee.amounts = 200000
    print(employee.amounts)
   
   
    # employee.showMessage()
    # employee._deposit(5000)
    # employee.__withdraw(50000)

