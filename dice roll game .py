import tkinter 
import random

root=tkinter.Tk()
root.geometry('600x600')
root.title('Roll Dice')

l1=tkinter.Label(root,text='',font=('Helvetica',260))


def rolldice():
    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.configure(text=f'{random.choice(dice)}{random.choice(dice)}')
    l1.pack()
b1=tkinter.Button(root,text="let's Roll dice...........",foreground='red',command=rolldice)
b1.place(x=330,y=0)
b1.pack()


root.mainloop()