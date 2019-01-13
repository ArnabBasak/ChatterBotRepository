from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)
engine = pyttsx3.init()
for files in os.listdir('F:/'):
    data = open('F:/reddit_data/2007/' + files,'r').readlines()
    bot.train(data)
    
while True:
    message = input('You: ')
    if message.strip() != 'Bye':
        reply = bot.get_response(message)
        print('Chatbot :',reply)
        engine.say(reply)
        engine.runAndWait()
        
    if message.strip() =='Bye':
        print('ChatBot : Bye')
        break