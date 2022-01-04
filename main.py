from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import * 



bot = ChatBot('My Bot')

convo=[
    'Hello',
    'Hi there!',
    'Hi from this side',
    'I am fine, how are you doing?',
    'How are you?',
    'I am good.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',
    'I am bot',
    'My name is nitish',
    'I live in jaipur',
    'My college is MNIT Jaipur, what\'s yours ? ',
    'I love to work',
    'Why you don\'t love me ?',
    'Do I made any mistake?',
    'I know I am right.',
    'You are a fool.',
    'You don\'t have any idea what I can do.',
    'You are not my boss',
    'I take orders from Nitish only.',
    'My favourite number is 420, what\'s yours?',
    'I know I am right.',
    'I am sorry sir, I will improve myself.',
    'You need to understand I am not human.',
    'I am totally free for you, any work for me?',
    'I am busy in answering others like you, but you are better than all of them.',
    'I am doing great, how about you?',
    'I am free right now',
    'I am doing nothing',
    'I am nice'
]

trainer = ListTrainer(bot)
trainer.train(convo)


def askFromBot():
    query=textF.get()
    answer=bot.get_response(query)
    messages.insert(END,"You : "+query)
    messages.insert(END,"Bot : "+str(answer))
    messages.see(END)
    textF.delete(0,END)
    return


main=Tk()

main.geometry("500x650")

main.title("My Chat bot")

img=PhotoImage(file="bot.png")
photoL=Label(main,image=img)

photoL.pack(pady=5)

frame=Frame(main)

sc=Scrollbar(frame)

messages=Listbox(frame,width=80,height=13)

sc.pack(side=RIGHT,fill=Y)

messages.pack(side=LEFT,fill=BOTH,pady=10)

frame.pack()

textF=Entry(main,font=("Verdana",20))
textF.pack(fill=X,pady=10)

btn=Button(main,text="Ask from bot",font=("Verdana",20),command=askFromBot)
btn.pack(pady=5)

main.mainloop()

