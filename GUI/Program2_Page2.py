from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import cv2

class Application:
    def __init__(self):

        self.vs = cv2.VideoCapture(0)
        self.root = tk.Tk()
        self.root.title("Program 2 (page 2)")
        self.root.minsize(width=497, height=945)
        self.root.resizable(width=0, height=0)
        self.root.protocol('WM_DELETE_WINDOW', self.destructor)

        self.panel = tk.Label(self.root)
        self.panel.pack(padx=10, pady=10)

        tree = ttk.Treeview(self.root, selectmode='browse')
        tree.place(x=40, y=663)

        vsb = ttk.Scrollbar(self.root, orient="vertical", command=tree.yview)
        vsb.place(x=241 + 200 + 2, y=660, height=210 + 20)
        tree.configure(yscrollcommand=vsb.set)

        tree["columns"] = ("1", "2", "3", "4")
        tree['show'] = 'headings'

        tree.column("1", width=100, anchor='c')
        tree.column("2", width=100, anchor='c')
        tree.column("3", width=100, anchor='c')
        tree.column("4", width=100, anchor='c')

        tree.heading("1", text="Chack")
        tree.heading("2", text="Name")
        tree.heading("3", text="ID")
        tree.heading("4", text="Status")

        tree.insert("", 'end', text="L1", values=("Walter", "White"))
        tree.insert("", 'end', text="L2", values=("Walter", "White"))
        tree.insert("", 'end', text="L3", values=("Walter", "White"))
        tree.insert("", 'end', text="L4", values=("Walter", "White"))
        tree.insert("", 'end', text="L5", values=("Walter", "White"))
        tree.insert("", 'end', text="L6", values=("Walter", "White"))
        tree.insert("", 'end', text="L7", values=("Walter", "White"))
        tree.insert("", 'end', text="L8", values=("Walter", "White"))
        tree.insert("", 'end', text="L9", values=("Walter", "White"))
        tree.insert("", 'end', text="L10", values=("Walter", "White"))
        tree.insert("", 'end', text="L11", values=("Walter", "White"))
        tree.insert("", 'end', text="L12", values=("Walter", "White"))
        tree.insert("", 'end', text="L13", values=("Walter", "White"))
        tree.insert("", 'end', text="L14", values=("Walter", "White"))
        tree.insert("", 'end', text="L15", values=("Walter", "White"))
        tree.insert("", 'end', text="L16", values=("Walter", "White"))
        tree.insert("", 'end', text="L17", values=("Walter", "White"))
        tree.insert("", 'end', text="L18", values=("Walter", "White"))
        tree.insert("", 'end', text="L19", values=("Walter", "White"))
        tree.insert("", 'end', text="L20", values=("Walter", "White"))
        tree.insert("", 'end', text="L21", values=("Walter", "White"))
        tree.insert("", 'end', text="L22", values=("Walter", "White"))
        tree.insert("", 'end', text="L23", values=("Walter", "White"))
        tree.insert("", 'end', text="L24", values=("Walter", "White"))
        tree.insert("", 'end', text="L25", values=("Walter", "White"))
        tree.insert("", 'end', text="L26", values=("Walter", "White"))

        Button1 = tk.Button(text="Print", height=2, width=50)
        Button1.pack(side='bottom', padx=5, pady=5)

        self.loop()

    def loop(self):
        global frame, Result, p,  frame2
        global threshold1,threshold2,areaMin,areaMax
        threshold1 = cv2.getTrackbarPos("threshold1", "Parameters")
        threshold2 = cv2.getTrackbarPos("threshold2", "Parameters")
        areaMin = cv2.getTrackbarPos("areaMin", "Parameters")
        areaMax = cv2.getTrackbarPos("areaMax", "Parameters")
        ret, frame = self.vs.read()
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        Result = frame.copy()
        frame2 = frame.copy()
        Result = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        self.frame = Image.fromarray(Result)
        frame = ImageTk.PhotoImage(image=self.frame)
        self.panel.imgtk = frame
        self.panel.config(image=frame)
        self.root.after(1, self.loop)

    def destructor(self):
        self.root.destroy()
        self.vs.release()
        cv2.destroyAllWindows()

pba = Application()
pba.root.mainloop()
