#!pip install bs4
from bs4 import BeautifulSoup as bs
import requests

root = 'https://www.vocabulary.com/dictionary/'

def diction(y):
    res = ''
    url = root+y
    r = requests.get(url)
    soup = bs(r.content,"lxml")
    definitions = soup.find_all("h3",{"class":"definition"})
    if len(definitions)==0:
        res += "Word not found."
        return res
    else:
        for i in definitions:
            res += i.text
        return res

def send():
    msg = Entrybox.get("1.21","end-1c")
    Entrybox.delete("0.0",END)

    if msg != '':
        Chatlog.config(state=NORMAL)
        Chatlog.delete("0.0",END)
        Chatlog.insert(END,"Word:"+ msg + '\n\n')
        Chatlog.config(foreground="#442265",font=("Verdana",12))

        res = diction(msg)
        Chatlog.insert(END,"Meaning:"+ res + '\n\n')

        Chatlog.config(state=NORMAL)


from tkinter import *
top = Tk()
top.geometry('400x600')
top.resizable(height=FALSE,width=FALSE)
top.title("Dictionary")
top.configure(bg='yellow')

#Bind scrollbar to Chat window
scroll = Scrollbar(top)
scroll.place(x=369,y=6,height=430)

#Create Chat window
Chatlog = Text(top,bd=0,bg='white',width=50,height=8,font='Arial',yscrollcommand=scroll.set)
Chatlog.config(state=DISABLED)
Chatlog.place(x=20,y=6,height=430,width=350)

scroll.config(command=Chatlog.yview())

#Create button to tell the bot
B = Button(top,text="OK",width=10,height=2,bg='green',command=send)

#Create box to enter text
Entrybox = Text(top,bd=0,bg='white',width=29,height=5,font='Arial')
Entrybox.insert(END,"Enter the word here: ")
Entrybox.bind('<Return>',None)


#Place all components in screen
#scroll.pack(side=RIGHT,fill=Y)
Entrybox.place(x=20,y=455,height=90,width=360)
B.place(x=310,y=550)

top.mainloop()