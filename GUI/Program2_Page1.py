from tkinter import *
from tkinter import ttk
import tkinter as tk

win = tk.Tk()
win.title("Program 2 (page 1)")
win.minsize(width=460, height=580)
win.resizable(width=0, height=0)

tree = ttk.Treeview(win, selectmode='browse')
tree.place(x=40, y=30)

vsb = ttk.Scrollbar(win, orient="vertical", command=tree.yview)
vsb.place(x=140+200+2, y=28, height=210+20)
tree.configure(yscrollcommand=vsb.set)

tree["columns"] = ("1", "2", "3")
tree['show'] = 'headings'

tree.column("1", width=60, anchor='c')
tree.column("2", width=150, anchor='c')
tree.column("3", width=150, anchor='c')

tree.heading("1", text="")
tree.heading("2", text="Name")
tree.heading("3", text="ID")

tree.insert("",'end',text="L1",values=("", "A", "0001"))

###############################################################################################

tree1 = ttk.Treeview(win, selectmode='browse')
tree1.place(x=40, y=292)

vsb1 = ttk.Scrollbar(win, orient="vertical", command=tree1.yview)
vsb1.place(x=140+200+2, y=290, height=210+20)
tree1.configure(yscrollcommand=vsb1.set)

tree1["columns"] = ("1", "2", "3")
tree1['show'] = 'headings'

tree1.column("1", width=120, anchor='c')
tree1.column("2", width=120, anchor='c')
tree1.column("3", width=120, anchor='c')

tree1.heading("1", text="Name")
tree1.heading("2", text="ID")
tree1.heading("3", text="Number")

tree1.insert("",'end',text="L1",values=("Z", "0001", "XXX"))

Button(text="BUTTON (NEXT TO PAGE 2)", bd=5).pack(side='bottom', ipadx=40, ipady=0, padx=5, pady=5)

class Table:
    lst = []
    def __init__(self, root):
        super().__init__()

    def setRow(self, row) :
        lst.append(row)


    
win.mainloop()

