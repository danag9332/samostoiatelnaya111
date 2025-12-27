from tkinter import *
from tkinter import messagebox

okno = Tk()
okno.title("Крестики-нолики")

khodit = "X"

pole = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

for i in range(3):
    for j in range(3):
        btn = Button(okno, text=" ", font=("Arial", 30), width=3, height=1)
        btn.grid(row=i, column=j)
        
        def klik(event, r=i, c=j):
            global khodit
            
            if pole[r][c] == " ":
                pole[r][c] = khodit
                event.widget.config(text=khodit)
                
                pobeda = False
                
                if pole[0][0] == khodit and pole[0][1] == khodit and pole[0][2] == khodit:
                    pobeda = True
                if pole[1][0] == khodit and pole[1][1] == khodit and pole[1][2] == khodit:
                    pobeda = True
                if pole[2][0] == khodit and pole[2][1] == khodit and pole[2][2] == khodit:
                    pobeda = True
                    
                if pole[0][0] == khodit and pole[1][0] == khodit and pole[2][0] == khodit:
                    pobeda = True
                if pole[0][1] == khodit and pole[1][1] == khodit and pole[2][1] == khodit:
                    pobeda = True
                if pole[0][2] == khodit and pole[1][2] == khodit and pole[2][2] == khodit:
                    pobeda = True
                    
                if pole[0][0] == khodit and pole[1][1] == khodit and pole[2][2] == khodit:
                    pobeda = True
                if pole[0][2] == khodit and pole[1][1] == khodit and pole[2][0] == khodit:
                    pobeda = True
                
                if pobeda:
                    messagebox.showinfo("Игра окончена", khodit + " выиграл!")
                    for child in okno.winfo_children():
                        if isinstance(child, Button):
                            child.config(state=DISABLED)
                    return
                
                nichya = True
                for row in pole:
                    for cell in row:
                        if cell == " ":
                            nichya = False
                            
                if nichya:
                    messagebox.showinfo("Игра окончена", "Ничья!")
                    for child in okno.winfo_children():
                        if isinstance(child, Button):
                            child.config(state=DISABLED)
                    return
                
                if khodit == "X":
                    khodit = "O"
                else:
                    khodit = "X"
        
        btn.bind("<Button-1>", klik)

okno.mainloop()