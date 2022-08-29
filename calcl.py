from tkinter import *


class Calc(Tk):
    def __init__(self):
        super(Calc, self).__init__()
        listbtn = []
        self.title('Calc')
        self.geometry('310x260')
        self.ent = Entry(justify=RIGHT, font=('Arial', 20))
        self.ent.grid(row=0, columnspan=6)
        oper = [[], ['7', '8', '9', '/', 'AC', 'C'],
                ['4', '5', '6', '*', '(', ')'],
                ['1', '2', '3', '-', 'sqrt', 'x²'],
                ['0', '.', '%', '+', '=', '=']]

        for row in range(1, 5):
            for column in range(6):
                self.textButton = oper[row][column]
                func = lambda text=self.textButton: self.add_digit(text)
                self.btn = Button(text=f'{self.textButton}', bg='white', height=3, width=6, command=func)
                self.btn.grid(row=row, column=column)
                listbtn.append(self.btn)

        listbtn[23].destroy()
        listbtn[22].grid_configure(columnspan=2)
        listbtn[22].config(width=14, command=self.calculate)
        listbtn[4].config(command=self.clear_all)
        listbtn[5].config(command=self.clear)
        listbtn[17].config(command=self.multi)
        listbtn[16].config(text='√(x)', command=self.sqrt)
        listbtn[20].config(command=self.pers)
        """ 
                self.btn1 = Button(text=f'7', bg='white', height=3, width=6)
                self.btn1.grid(row=1,column =0)
                self.btn2 = Button(text=f'8', bg='white', height=3, width=6)
                self.btn2.grid(row=1, column=1)
                self.btn3 = Button(text=f'9', bg='white', height=3, width=6)
                self.btn3.grid(row=1, column=2)
                self.btn4 = Button(text=f'/', bg='white', height=3, width=6)
                self.btn4.grid(row=1, column=3)
                self.btn5 = Button(text=f'AC', bg='white', height=3, width=6)
                self.btn5.grid(row=1, column=4)
                self.btn6 = Button(text=f'C', bg='white', height=3, width=6)
                self.btn6.grid(row=1, column=5)"""
        self.mainloop()

    def add_digit(self, text):
        if (text in '/*-+()') and (self.ent.get()[-1] == text):
            text = ''
        self.ent.insert(END, f'{text}')
        if self.ent.get() == '':
            self.ent.insert(END, f'{text}')

    def clear(self):
        len_text = len(self.ent.get())
        self.ent.delete(len_text - 1, END)

    def clear_all(self):
        self.ent.delete(0, END)

    def calculate(self):
        x = eval(self.ent.get())
        self.ent.delete(0, END)
        if int(x) == x:
            self.ent.insert(0, int(x))
        else:
            self.ent.insert(0, x)

    def multi(self):
        x = eval(self.ent.get())
        self.ent.delete(0, END)
        self.ent.insert(0, x * x)

    def sqrt(self):
        x = eval(self.ent.get())
        self.ent.delete(0, END)
        y = x**0.5
        if int(y) == y:
            self.ent.insert(0, int(y))
        else:
            self.ent.insert(0, y)

    def pers(self):
        x = eval(self.ent.get())
        self.ent.delete(0, END)
        self.ent.insert(0, (x * 0.01))


root = Calc()
