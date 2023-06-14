from  tkinter import *
from tkinter import messagebox

clicked = True #можно кликать\нажимать
count = 0 #для счета


razmerdisplay = "times, 20"

def checkWinner():
    global winner #глобальные перемен. - это те к которым можно обращаться и за этой фнукцией
    winner = False #по началу победитель неизвестен

    if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X":
        button1.config(bg="lime")# (X) (X) (X)    config - edit, редактировать
        button2.config(bg="lime")# (0) (0) (0)  
        button3.config(bg="lime")# (0) (0) (0) 
        winner = True #победитель известен
        messagebox.showinfo("Game over", "p1 win")
        start()
        #done
    elif button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X":
        button4.config(bg="lime")# (0) (0) (0)    config - edit, редактировать
        button5.config(bg="lime")# (X) (X) (X)  
        button6.config(bg="lime")# (0) (0) (0) 
        winner = True #победитель известен
        messagebox.showinfo("Game over", "p1 win")
        start()
        #done
    elif button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X":
        button7.config(bg="lime")# (0) (0) (0)    config - edit, редактировать
        button8.config(bg="lime")# (0) (0) (0)
        button9.config(bg="lime")# (X) (X) (X) 
        winner = True #победитель известен
        messagebox.showinfo("Game over", "p1 win")
        start()
        #done

    elif button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X":
        button1.config(bg="lime")# (X) (0) (0)    config - edit, редактировать
        button4.config(bg="lime")# (X) (0) (0)  
        button7.config(bg="lime")# (X) (0) (0) 
        winner = True #победитель известен
        messagebox.showinfo("Game over", "p1 win")
        start()
        #done

    elif button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X":
        button2.config(bg="lime")# (0) (X) (0)    config - edit, редактировать
        button5.config(bg="lime")# (0) (X) (0)  
        button8.config(bg="lime")# (0) (X) (0) 
        winner = True #победитель известен
        messagebox.showinfo("Game over", "p1 win")
        start()
        #done

    elif button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X":
        button3.config(bg="lime")# (0) (0) (X)    config - edit, редактировать
        button6.config(bg="lime")# (0) (0) (X)  
        button9.config(bg="lime")# (0) (0) (X) 
        winner = True #победитель известен
        messagebox.showinfo("Game over", "p1 win")
        start()
        #done

    elif button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X":
        button1.config(bg="lime")# (X) (0) (0)    config - edit, редактировать
        button5.config(bg="lime")# (0) (X) (0)  
        button9.config(bg="lime")# (0) (0) (X) 
        winner = True #победитель известен
        messagebox.showinfo("Game over", "p1 win")
        start()
        #done

    elif button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X":
        button3.config(bg="lime")# (0) (0) (X)    config - edit, редактировать
        button5.config(bg="lime")# (0) (X) (0)  
        button7.config(bg="lime")# (X) (0) (0) 
        winner = True #победитель известен
        messagebox.showinfo("Game over", "p1 win")
        start()
        #done
    #krestiki done

    elif button1["text"] == "0" and button2["text"] == "0" and button3["text"] == "0":
        button1.config(bg="lime")# (X) (X) (X)    config - edit, редактировать
        button2.config(bg="lime")# (0) (0) (0)  
        button3.config(bg="lime")# (0) (0) (0) 
        winner = True #победитель известен
        messagebox.showinfo("Game over", "p2 win")
        start()
        #done
    elif button4["text"] == "0" and button5["text"] == "0" and button6["text"] == "0":
        button4.config(bg="lime")# (0) (0) (0)    config - edit, редактировать
        button5.config(bg="lime")# (X) (X) (X)  
        button6.config(bg="lime")# (0) (0) (0) 
        winner = True #победитель известен
        messagebox.showinfo("Game over", "p2 win")
        start()
        #done
    elif button7["text"] == "0" and button8["text"] == "0" and button9["text"] == "0":
        button7.config(bg="lime")# (0) (0) (0)    config - edit, редактировать
        button8.config(bg="lime")# (0) (0) (0)  
        button9.config(bg="lime")# (X) (X) (X) 
        winner = True #победитель известен
        messagebox.showinfo("Game over", "p2 win")
        start()
        #done

    elif button1["text"] == "0" and button4["text"] == "0" and button7["text"] == "0":
        button1.config(bg="lime")# (X) (0) (0)    config - edit, редактировать
        button4.config(bg="lime")# (X) (0) (0)  
        button7.config(bg="lime")# (X) (0) (0) 
        winner = True #победитель известен
        messagebox.showinfo("Game over", "p2 win")
        start()
        #done

    elif button2["text"] == "0" and button5["text"] == "0" and button8["text"] == "0":
        button2.config(bg="lime")# (0) (X) (0)    config - edit, редактировать
        button5.config(bg="lime")# (0) (X) (0)  
        button8.config(bg="lime")# (0) (X) (0) 
        winner = True #победитель известен
        messagebox.showinfo("Game over", "p2 win")
        start()
        #done

    elif button3["text"] == "0" and button6["text"] == "0" and button9["text"] == "0":
        button3.config(bg="lime")# (0) (0) (X)    config - edit, редактировать
        button6.config(bg="lime")# (0) (0) (X)  
        button9.config(bg="lime")# (0) (0) (X) 
        winner = True #победитель известен
        messagebox.showinfo("Game over", "p2 win")
        start()
        #done

    elif button1["text"] == "0" and button5["text"] == "0" and button9["text"] == "0":
        button1.config(bg="lime")# (X) (0) (0)    config - edit, редактировать
        button5.config(bg="lime")# (0) (X) (0)  
        button9.config(bg="lime")# (0) (0) (X) 
        winner = True #победитель известен
        messagebox.showinfo("Game over", "p2 win")
        start()
        #done

    elif button3["text"] == "0" and button5["text"] == "0" and button7["text"] == "0":
        button3.config(bg="lime")# (0) (0) (X)    config - edit, редактировать
        button5.config(bg="lime")# (0) (X) (0)  
        button7.config(bg="lime")# (X) (0) (0) 
        winner = True #победитель известен
        messagebox.showinfo("Game over", "p2 win")
        start()
        #done

def checkDraw():
    global winner, count #перемен победителя и счётчик
    if winner == False and count == 9: #winner(победителя нет), count(все 9 клеток занято без победителя)
        messagebox.showinfo("Game over", "Draw!") #Коробка с инфой
        start()


def buttonClicked(button):
    global clicked, count
    if button["text"] == " " and clicked == True: #если пусто(не нажата) и нажимаем
        button["text"] = "X" #появляется X
        clicked = False #нажатие аннулируется
        count += 1 #добавляется счетъ
        checkDraw()                                                                                                                                                                                                                     
        checkWinner() #проверяем наличие победителя

    elif button["text"] == " " and clicked == False: #если пусто(не нажата) и нажимаем
        button["text"] = "0" #появляется 0
        clicked = True #нажатие аннулируется
        count += 1 #добавляется счет
        checkWinner() #проверяем наличие победителя
        checkDraw()                                                                                                                                                                                                                     

    else:
        messagebox.showerror("", "")

def start(): #функция старт
    #объявляем кнопки глобально
    global button1, button2, button3, button4, button5, button6, button7, button8, button9 
    global clicked, count #global чтобы обращатся и за пределами функции
    clicked = True # x начинает первым 
    count = 0 #счётчик начинается с нуля

    #дальше добавляем кнопки
    button1 = Button(display, bg="#ccc", font=razmerdisplay, fg="tomato", text=" ", width=15, height=6, command=lambda: buttonClicked(button1)) #перемен для кнопки1
    button1.grid(row=0, column=0) #сетка 
    button2 = Button(display, bg="#ccc", font=razmerdisplay, fg="tomato", text=" ", width=15, height=6, command=lambda: buttonClicked(button2)) #перемен для кнопки1
    button2.grid(row=0, column=1) #сетка 
    button3 = Button(display, bg="#ccc", font=razmerdisplay, fg="tomato", text=" ", width=15, height=6, command=lambda: buttonClicked(button3)) #перемен для кнопки1
    button3.grid(row=0, column=2) #сетка 
    button4 = Button(display, bg="#ccc", font=razmerdisplay, fg="tomato", text=" ", width=15, height=6, command=lambda: buttonClicked(button4)) #перемен для кнопки1
    button4.grid(row=1, column=0) #сетка 
    button5 = Button(display, bg="#ccc", font=razmerdisplay, fg="tomato", text=" ", width=15, height=6, command=lambda: buttonClicked(button5)) #перемен для кнопки1
    button5.grid(row=1, column=1) #сетка 
    button6 = Button(display, bg="#ccc", font=razmerdisplay, fg="tomato", text=" ", width=15, height=6, command=lambda: buttonClicked(button6)) #перемен для кнопки1
    button6.grid(row=1, column=2) #сетка 
    button7 = Button(display, bg="#ccc", font=razmerdisplay, fg="tomato", text=" ", width=15, height=6, command=lambda: buttonClicked(button7)) #перемен для кнопки1
    button7.grid(row=2, column=0) #сетка 
    button8 = Button(display, bg="#ccc", font=razmerdisplay, fg="tomato", text=" ", width=15, height=6, command=lambda: buttonClicked(button8)) #перемен для кнопки1
    button8.grid(row=2, column=1) #сетка 
    button9 = Button(display, bg="#ccc", font=razmerdisplay, fg="tomato", text=" ", width=15, height=6, command=lambda: buttonClicked(button9)) #перемен для кнопки1
    button9.grid(row=2, column=2) #сетка 


display = Tk() #интерфейс внутри перемен
display.title("XO") #название прилож

start()
display.mainloop()