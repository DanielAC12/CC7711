from chatbot import Chatbot

myChatBot = Chatbot()
myChatBot.createModel()

print('Oi tudo bem')
pergunta = input('Como posso te ajudar? ')
resposta, intecao = myChatBot.chatbot_response(pergunta)
print(resposta + "  ["+intecao[0]['intent']+"]")

while(intecao[0]['intent']!="despedida"):
  pergunta = input('Posso te ajudar em algo mais? ')
  resposta, intecao = myChatBot.chatbot_response(pergunta)
  print(resposta + "  ["+intecao[0]['intent']+"]")

print('Tamo junto')
