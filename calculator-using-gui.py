import tkinter
from tkinter import *
expression=""
def press(num):
  global expression
  expression=expression+str(num)
  equation.set(expression)
def equalpress():
  try:
    global expression
    total=str(eval(expression))
    equation.set(total)
    expression=""
  except:
    equation.set("error")
    expression=""
def clear():
  global expression
  expression=""
  equation.set("")
if __name__ == "__main__":
         m=Tk()
         m.title("Calculator")
         equation=StringVar()
         exp_field=Entry(m,textvariable=equation)
         exp_field.grid(columnspan=4,ipadx=70)
         b1=Button(m,text='1',width=6,command=lambda: press(1),bg='yellow',fg='black')
         b1.grid(row=3,column=0)
         b2=Button(m,text='2',width=6,command=lambda: press(2),bg='yellow',fg='black')
         b2.grid(row=3,column=1)
         b3=Button(m,text='3',width=6,command=lambda: press(3),bg='yellow',fg='black')
         b3.grid(row=3,column=2)
         ba=Button(m,text='+',width=6,command=lambda: press("+"),bg='yellow',fg='black')
         ba.grid(row=3,column=3)
         b4=Button(m,text='4',width=6,command=lambda: press(4),bg='yellow',fg='black')
         b4.grid(row=4,column=0)
         b5=Button(m,text='5',width=6,command=lambda: press(5),bg='yellow',fg='black')
         b5.grid(row=4,column=1)
         b6=Button(m,text='6',width=6,command=lambda: press(6),bg='yellow',fg='black')
         b6.grid(row=4,column=2)
         bb=Button(m,text='-',width=6,command=lambda: press("-"),bg='yellow',fg='black')
         bb.grid(row=4,column=3)
         b7=Button(m,text='7',width=6,command=lambda: press(7),bg='yellow',fg='black')
         b7.grid(row=5,column=0)
         b8=Button(m,text='8',width=6,command=lambda: press(8),bg='yellow',fg='black')
         b8.grid(row=5,column=1)
         b9=Button(m,text='9',width=6,command=lambda: press(9),bg='yellow',fg='black')
         b9.grid(row=5,column=2)
         bc=Button(m,text='/',width=6,command=lambda: press("/"),bg='yellow',fg='black')
         bc.grid(row=5,column=3)
         b0=Button(m,text='0',width=6,command=lambda: press(0),bg='yellow',fg='black')
         b0.grid(row=6,column=0)
         bd=Button(m,text='*',width=6,command=lambda: press("*"),bg='yellow',fg='black')
         bd.grid(row=6,column=1)
         be=Button(m,text='%',width=6,command=lambda: press("%"),bg='yellow',fg='black')
         be.grid(row=6,column=2)
         equal=Button(m,text='=',width=6,command=equalpress,bg='yellow',fg='black')
         equal.grid(row=6,column=3)
         clear=Button(m,text='Clear',width=6,command=clear,bg='yellow',fg='black')
         clear.grid(row=7,columnspan=4)

         m.mainloop

