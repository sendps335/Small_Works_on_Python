from tkinter import *
import random
import numpy

global tot
global val
tot=0

def interface():
    global val
    val=dict()# For Mapping of the Grid System
    tk=Tk()
    tk.config(bg="yellow")
    tk.title("MineSweeper-DPS")
    tk.resizable(0,0)
    #Creating the Buttons
    #As this is a 6x6 Minesweeper Interface
    b11=Button(tk,height=1,width=2,command=lambda:game(b11,tk)) #Button at Grid[1,1]
    b12=Button(tk,height=1,width=2,command=lambda:game(b12,tk)) #Button at Grid[1,2]
    b13=Button(tk,height=1,width=2,command=lambda:game(b13,tk)) #...
    b14=Button(tk,height=1,width=2,command=lambda:game(b14,tk)) #...
    b15=Button(tk,height=1,width=2,command=lambda:game(b15,tk)) #...
    b16=Button(tk,height=1,width=2,command=lambda:game(b16,tk)) #...
    b21=Button(tk,height=1,width=2,command=lambda:game(b21,tk)) #...
    b22=Button(tk,height=1,width=2,command=lambda:game(b22,tk)) #...
    b23=Button(tk,height=1,width=2,command=lambda:game(b23,tk)) #...
    b24=Button(tk,height=1,width=2,command=lambda:game(b24,tk)) #...
    b25=Button(tk,height=1,width=2,command=lambda:game(b25,tk)) #...
    b26=Button(tk,height=1,width=2,command=lambda:game(b26,tk)) #...
    b31=Button(tk,height=1,width=2,command=lambda:game(b31,tk)) #...
    b32=Button(tk,height=1,width=2,command=lambda:game(b32,tk)) #...
    b33=Button(tk,height=1,width=2,command=lambda:game(b33,tk)) #...
    b34=Button(tk,height=1,width=2,command=lambda:game(b34,tk)) #...
    b35=Button(tk,height=1,width=2,command=lambda:game(b35,tk)) #...
    b36=Button(tk,height=1,width=2,command=lambda:game(b36,tk)) #...
    b41=Button(tk,height=1,width=2,command=lambda:game(b41,tk)) #...
    b42=Button(tk,height=1,width=2,command=lambda:game(b42,tk)) #...
    b43=Button(tk,height=1,width=2,command=lambda:game(b43,tk)) #...
    b44=Button(tk,height=1,width=2,command=lambda:game(b44,tk)) #...
    b45=Button(tk,height=1,width=2,command=lambda:game(b45,tk)) #...
    b46=Button(tk,height=1,width=2,command=lambda:game(b46,tk)) #...
    b51=Button(tk,height=1,width=2,command=lambda:game(b51,tk)) #...
    b52=Button(tk,height=1,width=2,command=lambda:game(b52,tk)) #...
    b53=Button(tk,height=1,width=2,command=lambda:game(b53,tk)) #...
    b54=Button(tk,height=1,width=2,command=lambda:game(b54,tk)) #...
    b55=Button(tk,height=1,width=2,command=lambda:game(b55,tk)) #...
    b56=Button(tk,height=1,width=2,command=lambda:game(b56,tk)) #...
    b61=Button(tk,height=1,width=2,command=lambda:game(b61,tk)) #...
    b62=Button(tk,height=1,width=2,command=lambda:game(b62,tk)) #...
    b63=Button(tk,height=1,width=2,command=lambda:game(b63,tk)) #...
    b64=Button(tk,height=1,width=2,command=lambda:game(b64,tk)) #...
    b65=Button(tk,height=1,width=2,command=lambda:game(b65,tk)) #...
    b66=Button(tk,height=1,width=2,command=lambda:game(b66,tk)) #...
    #Create the Grid/ Position of the Buttons on the Interface
    # i.e. Assign the Positions to the button on the Interface
    b11.grid(row=1,column=1)
    b12.grid(row=1,column=2)
    b13.grid(row=1,column=3)
    b14.grid(row=1,column=4)
    b15.grid(row=1,column=5)
    b16.grid(row=1,column=6)
    b21.grid(row=2,column=1)
    b22.grid(row=2,column=2)
    b23.grid(row=2,column=3)
    b24.grid(row=2,column=4)
    b25.grid(row=2,column=5)
    b26.grid(row=2,column=6)
    b31.grid(row=3,column=1)
    b32.grid(row=3,column=2)
    b33.grid(row=3,column=3)
    b34.grid(row=3,column=4)
    b35.grid(row=3,column=5)
    b36.grid(row=3,column=6)
    b41.grid(row=4,column=1)
    b42.grid(row=4,column=2)
    b43.grid(row=4,column=3)
    b44.grid(row=4,column=4)
    b45.grid(row=4,column=5)
    b46.grid(row=4,column=6)
    b51.grid(row=5,column=1)
    b52.grid(row=5,column=2)
    b53.grid(row=5,column=3)
    b54.grid(row=5,column=4)
    b55.grid(row=5,column=5)
    b56.grid(row=5,column=6)
    b61.grid(row=6,column=1)
    b62.grid(row=6,column=2)
    b63.grid(row=6,column=3)
    b64.grid(row=6,column=4)
    b65.grid(row=6,column=5)
    b66.grid(row=6,column=6)
    ### Putting the Game Algorithm
    button_list=[b11,b12,b13,b14,b15,b16,b21,b22,b23,b24,b25,b26,b31,b32,b33,b34,b35,b36,b41,b42,b43,b44,b45,b46,b51,b52,b53,b54,b55,b56,b61,b62,b63,b64,b65,b66]
    val1=['1']*(6)
    val2=['2']*(6)
    val3=['3']*(6)
    val4=['4']*(6)
    val5=['5']*(6)
    val_bomb=['bomb']*(6)
    net_val=val1+val2+val3+val4+val5+val_bomb
    random.shuffle(net_val)
    #print(net_val)
    for i in range(0,len(net_val)):
        val[button_list[i]]=net_val[i]
    
def game(button,tk):
    global val,tot
    if(val[button]=='bomb'):
        tk.destroy()
        tk_end=Tk()
        tk_end.config(bg="yellow")
        tk_end.title("Mine-Sweeper-DPS")
        tk_end.resizable(0,0)
        label=Label(tk_end,text=str(tot))
        label.grid(row=1,column=1)
        label2=Label(tk_end,text="GameOver!")
        label2.grid(row=2,column=1)
    else:
        if(val[button] != '-1'):
            button['text']=val[button]
            tot=tot+int(val[button])
            val[button]='-1'
            if(tot==90):
                tk.destroy()
                tk_end=Tk()
                tk_end.config(bg="yellow")
                tk_end.title("MineSweeper-DPS")
                tk_end.resizable(0,0)
                label1=Label(tk_end,text="You Won!!")
                label1.grid(row=1,column=1)
                label2=Label(tk_end,text="Net Score = 90")
                label2.grid(row=2,column=1)

if __name__=="__main__":
    interface()