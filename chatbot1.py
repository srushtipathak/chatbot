from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot= ChatBot(' Bot ')
bot.set_trainer(ListTrainer)

for files in os.listdir('D:/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
    data = open('D:\chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/' + files, 'r').readlines()
    bot.train(data)

while True:
    msg = input(' YOU : ' )
    if msg.strip() !='Bye':
        reply = bot.get_response(msg)
        print(' Chatbot : ',reply)
    if msg.strip()=='Bye':
        print(' Chatbot : Byeeeeeee')
        break
