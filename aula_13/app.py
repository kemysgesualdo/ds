from tkinter import 

class App:
    def __init__(self, root):
        self.frame1 = frame(root)
        self.frame1.pack()
        label(self,frame1,text="Conversãode Centimetro para polegada",
        font=("Verdana", "14", "bold"), height=3).pack()

        Label(self.frame1,text="Centimetro(s):").pack(side=LEFT)
        self.centimetro=Entry(self.frame1)
        self.centimetro.focus_force()
        self.centimetro.pack(side=LEFT)
        Button(self,frame1,text="Converter", command=self.converter)

        Label(self.frame1,text="Polegada(s):").pack(side=LEFT)