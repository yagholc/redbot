
from telebot import types
import telebot
import time
try:
    @bot.message_handler(func=lambda msg: (msg.text == "Iniciar"))
    def intro(msg):
        # markup = types.ReplyKeyboardRemove(selective=False)
        # tb.send_message(chat_id, message, reply_markup=markup)
        # message=bot.send_message(msg.chat.id, "Choose one letter:", reply_markup=markup, one_time_keyboard=True)
        message = bot.send_message(msg.chat.id, "Olá, eu sou o assistente virtual do Ame +. Em que posso ajuda-l@?",
                                reply_markup=setMarkup(["Consultar informações da conta", "Tenho uma dúvida"]))
        bot.register_next_step_handler(message, branchHandler1)


    def branchHandler1(msg):
        if msg.text == "Consultar informações da conta":
            getInfo(msg)
            
        elif msg.text == "Tenho uma dúvida":
            issueHandler(msg)


    def getInfo(msg):
        message = bot.send_message(msg.chat.id, "Selecione a opção desejada.",
                                reply_markup=setMarkup(["Saldo", "Beneficios adquiridos", "Desafios", "Cashback acumulado", "Meus cupons"]))
        bot.register_next_step_handler(message, branchHandler2)


    def issueHandler(msg):
        message = bot.send_message(msg.chat.id, "Selecione a opção desejada.",
                                reply_markup=setMarkup(["Resumo de funcionalidades", "Alteração de cadastro"]))
        bot.register_next_step_handler(message, branchHandler2)

    def branchHandler2(msg):
        msgDict = {"Resumo de funcionalidades": "resumo(msg)",
                "Alteração de cadastro": "altera_cadastro(msg)",
                "Saldo" : "saldo(msg)",
                "Beneficios adquiridos" : "beneficios(msg)",
                "Desafios" : "desafios(msg)",
                "Cashback acumulado" : "cashback(msg)",
                "Meus cupons" : "cupons(msg)"
                }
        
        eval(msgDict[msg.text])
        
        
            
    def resumo(msg):
        msg = bot.send_message(msg.chat.id,
                                "Resumo")

    def altera_cadastro(msg):
        msg = bot.send_message(msg.chat.id,
                                "Cadastro")

    def saldo(msg):
        msg = bot.send_message(msg.chat.id,
                                "Saldo")

    def beneficios(msg):
        msg = bot.send_message(msg.chat.id,
                                "Beneficios")

    def desafios(msg):
        msg = bot.send_message(msg.chat.id,
                                "desafios")

    def cashback(msg):
        msg = bot.send_message(msg.chat.id,
                                "Cashback")

    def cupons(msg):
        msg = bot.send_message(msg.chat.id,
                                "Cupons")
except:
    pass