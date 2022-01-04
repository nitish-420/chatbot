from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import * 
import speech_recognition as S
import pyttsx3 as pp
import threading

engine=pp.init()

voices=engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 125)

volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
engine.setProperty('volume',0.5)    # setting up volume level  between 0 and 1


def speak(word):
    engine.say(word)
    engine.runAndWait()

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


def takeQuery():
    sr=S.Recognizer()
    sr.pause_threshold=1
    print("your bot is listening ....")
    with S.Microphone() as m:
        try:
            audio=sr.listen(m)
            query=sr.recognize_google(audio,language='eng-in')
            textF.delete(0,END)
            textF.insert(0,query)

            askFromBot(query)
        except Exception as e:
            print(e)



def askFromBot(q=''):
    query=q if len(q) else textF.get()
    answer=bot.get_response(query)
    messages.insert(END,"You : "+query)
    speak(answer)
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

messages=Listbox(frame,width=80,height=13,yscrollcommand=sc.set)

sc.pack(side=RIGHT,fill=Y)

messages.pack(side=LEFT,fill=BOTH,pady=10)

frame.pack()

textF=Entry(main,font=("Verdana",20))
textF.pack(fill=X,pady=10)


btn=Button(main,text="Ask from bot",font=("Verdana",20),command=askFromBot)
btn.pack(pady=5)


def enterFunction(event):
    btn.invoke()

# going to bind main window with enter key
main.bind('<Return>',enterFunction)

def repeatListen():
    while True:
        takeQuery()

t=threading.Thread(target=repeatListen)
t.start()

main.mainloop()

