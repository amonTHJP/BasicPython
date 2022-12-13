from tkinter import * 
from tkinter import ttk, messagebox

GUI = Tk()
GUI.title("คำนวณราคาปลา")
GUI.geometry('700x600')

bg = PhotoImage(file='car.png')

BG = Label(GUI, image=bg)
BG.pack()

L = Label(GUI,text='กรุณากรอกจำนวนปลา (กิโลกรัม)',font=(None,20))
L.pack()

v_Quantity = StringVar() #เป็นตัวแปรที่เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
E1 = ttk.Entry(GUI, textvariable=v_Quantity, font=(None,20))
E1.pack()

def Cal():
    try:
        quan = float(v_Quantity.get())
        calc = quan * 39
        messagebox.showinfo("ราคาทั้งหมด","ราคาปลาทั้งหมด {} บาท".format(calc))
        result.configure(text=calc)
        E1.focus()

    except:
        messagebox.showwarning("กรอกผิด","กรุณากรอกเฉพาะตัวเลขเท่านั้น")
        v_Quantity.set("")


result = ttk.Label(GUI, font=(None,20))
result.pack()

B = ttk.Button(GUI, text='คำนวณ', command=Cal)
B.pack(ipadx=30, ipady=20) #ขยายความกว้าง x/y



GUI.mainloop()