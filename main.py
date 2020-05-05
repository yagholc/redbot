from telebot import types
import telebot
import time
import yaml
import updateJason
#from pydub import AudioSegment
#import speech_recognition as sr
with open(r"c\config.yml", "r") as ymlfile:
             cfg = yaml.load(ymlfile)


bot = telebot.TeleBot(cfg["token"]["red"])
respostas = list()

def setMarkup(opt, resize=(0.8, 0.5)):  # opt é uma lista de strings com as opções
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=resize)
    cmd = ''
    if isinstance(opt, list):
        if len(opt)==3:
            btn1 = types.KeyboardButton(opt[0])
            btn2 = types.KeyboardButton(opt[1])
            btn3 = types.KeyboardButton(opt[2])
            markup.add(btn1, btn2)
            markup.add(btn3)
            return(markup)
        else:
            itembtn = []
            for i in range(len(opt)):
                itembtn.append(types.KeyboardButton(opt[i]))
                #eval(f"itembtn{i} = types.KeyboardButton(opt[{i}])")
                cmd = cmd + f"itembtn[{i}], "
            return (eval('markup.row(' + cmd[0:-2] + ')'))
    else:
        itembtnY = types.KeyboardButton(opt)
        return (markup.row(itembtnY))



@bot.message_handler(commands=["start"])
def send_welcome(msg):
    # bot.reply_to(msg, "Clique no botão para iniciar seu processo de subscrição.")
    # markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    userID = msg.from_user.id #ID do usuario
    listIDs = updateJason.getAllIds()
    if userID in listIDs:
        #itembtn = types.KeyboardButton("Iniciar")
        # bot.send_message(msg.chat.id, "Clique no botão para iniciar uma nova experiência nas lojas Americanas.",
        #                 reply_markup=markup.row(itembtn))
        intro(msg)
    else:
        # itembtn = types.KeyboardButton("Ainda não tenho uma conta")
        # itembtn2 = types.KeyboardButton("Já tenho uma conta")
        bot.send_message(msg.chat.id, """Vejo que é a sua primeira vez conversando comigo, você já é um cliente Americanas cadastrado?.
                                        \nCaso não seja, não se preocupe! Você está a poucos cliques de poder participar dos nossos desafios""",
                        reply_markup=setMarkup(["Já tenho uma conta", "Ainda não tenho uma conta"]))
                        #reply_markup=markup.row([itembtn, itembtn2]))
        
                        
                    

@bot.message_handler(func=lambda msg: (msg.text == "Já tenho uma conta"))
def IDlink(msg):
    bot.send_message(msg.chat.id, "Ótimo! Só vou precisar do código gerado pelo seu app. ")
    bot.send_message(msg.chat.id, "OBS: Nesta versão trabalhamos com usuário pre-criados, digite um número de 0 a 9 para relaciona-lo ao seu usuário.")
    bot.register_next_step_handler(msg, intro2)

@bot.message_handler(func=lambda msg: (msg.text == "Ainda não tenho uma conta"))
def createAcc(msg):
    itembtn = types.KeyboardButton("Pronto")
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    bot.send_message(msg.chat.id, "Clique no link para se cadastrar na americanas")
    bot.send_message(msg.chat.id, r"Clique [aqui](https://cliente.americanas.com.br/simple-login/cadastro/pf?next=https%3A%2F%2Fwww.americanas.com.br%2F)", parse_mode='MarkdownV2')
    bot.send_message(msg.chat.id, "OBS: Como esse é apenas um protótipo é só aguardar alguns segundos para ser levado para a próxima fase!")
                    #parse_mode='MarkdownV2', reply_markup=markup.row(itembtn))
    time.sleep(4)
    IDlink(msg)
    #bot.register_next_step_handler(msg, IDlink)
    # bot.send_message(msg.chat.id, r"""Entendi, clicando neste link você poderá acessar a página de cadastro e assim poderá aproveitar as promoções do Ame +. 
    #         \n [Cadastro](https://cliente.americanas.com.br/simple-login/cadastro/pf?next=https%3A%2F%2Fwww.americanas.com.br%2F)""", parse_mode='MarkdownV2')
    #https://cliente.americanas.com.br/simple-login/cadastro/pf?next=https%3A%2F%2Fwww.americanas.com.br%2F

#Intro padrão
@bot.message_handler(func=lambda msg: (msg.text == "Iniciar"))
def intro(msg):
    # markup = types.ReplyKeyboardRemove(selective=False)
    # tb.send_message(chat_id, message, reply_markup=markup)
    # message=bot.send_message(msg.chat.id, "Choose one letter:", reply_markup=markup, one_time_keyboard=True)
    message = bot.send_message(msg.chat.id, "Olá, eu sou o assistente virtual Red. Em que posso ajuda-l@?",
                            reply_markup=setMarkup(["Consultar informações da conta", "Tenho uma dúvida"]))
    bot.register_next_step_handler(message, branchHandler1)

#intro para quem acabou de se cadastrar
def intro2(msg):
    # markup = types.ReplyKeyboardRemove(selective=False)
    # tb.send_message(chat_id, message, reply_markup=markup)
    # message=bot.send_message(msg.chat.id, "Choose one letter:", reply_markup=markup, one_time_keyboard=True)
    userID = msg.from_user.id 
    updateJason.setAccount(userID,msg.text)
    message = bot.send_message(msg.chat.id, "É ótimo te-l@ conosco, como posso ajudar?",
                            reply_markup=setMarkup(["Consultar informações da conta", "Tenho uma dúvida"]))
    bot.register_next_step_handler(message, branchHandler1)

#Intro para quem está voltando do final da arvore do bot
def intro3(msg):
    message = bot.send_message(msg.chat.id, "Fico feliz em poder ajuda-lo, mas se precisar é só chamar!",
                            reply_markup=setMarkup(["Consultar informações da conta", "Tenho uma dúvida"]))
    bot.register_next_step_handler(message, branchHandler1)

def branchHandler1(msg):
    if msg.text == "Consultar informações da conta":
        getInfo(msg)
        
    elif msg.text == "Tenho uma dúvida":
        issueHandler(msg)


def getInfo(msg):
    message = bot.send_message(msg.chat.id, "Selecione a opção desejada.",
                            reply_markup=setMarkup(["Saldo", "Beneficios adquiridos", "Desafios"], resize=(0.8, 0.5)))#"Cashback acumulado",



    bot.register_next_step_handler(message, branchHandler2)

@bot.message_handler(func=lambda msg: (msg.text.lower == "ajuda"))
def issueHandler(msg):
    message = bot.send_message(msg.chat.id, "Selecione a opção desejada.",
                            reply_markup=setMarkup(["Resumo de funcionalidades", "Alteração de cadastro"]))
    bot.register_next_step_handler(message, branchHandler2)

def branchHandler2(msg):
    msgDict = {"Resumo de funcionalidades": "resumo(msg)",
            "Alteração de cadastro": "altera_cadastro(msg)",
            "Saldo" : "saldo(msg)",
            "Beneficios adquiridos" : "beneficios(msg)",
            "Desafios" : "desafios(msg)"
            }
                       # "Cashback acumulado" : "cashback(msg)",
    
    eval(msgDict[msg.text])
    
    
        
def resumo(msg):
    msg = bot.send_message(msg.chat.id,
                            "Eu sou um assistente virtual e estou aqui para te guiar e fornecer informações por toda a sua jornada como cliente Americanas.", reply_markup=setMarkup(["Voltar começo"]))

    msg = bot.send_message(msg.chat.id,
                            "Nesse momento o que posso fazer é te apresentar relatórios dos beneficios e de seu andamento nos desafios.", reply_markup=setMarkup(["Voltar começo"]))
    bot.register_next_step_handler(msg, intro3)


def altera_cadastro(msg):
    msg = bot.send_message(msg.chat.id,
                            "Coming soon!", reply_markup=setMarkup(["Voltar começo"]))
    bot.register_next_step_handler(msg, intro3)

def saldo(msg):
    print(updateJason.consultData(msg.from_user.id,"nivel"))
    data = updateJason.consultData(msg.from_user.id,"nivel")
    bot.send_message(msg.chat.id, data)
    msg = bot.send_message(msg.chat.id,
                            "...", reply_markup=setMarkup(["Voltar começo"]))
    bot.register_next_step_handler(msg, intro3)

def beneficios(msg):
    print(updateJason.consultData(msg.from_user.id,"beneficios"))
    data = updateJason.consultData(msg.from_user.id,"beneficios")
    for dado in data:
        bot.send_message(msg.chat.id, dado)
    msg = bot.send_message(msg.chat.id,
                            "...", reply_markup=setMarkup(["Voltar começo"]))
    bot.register_next_step_handler(msg, intro3)

def desafios(msg):
    print(updateJason.consultData(msg.from_user.id,"desafios"))
    data = updateJason.consultData(msg.from_user.id,"desafios")
    for dado in data:
        bot.send_message(msg.chat.id, dado)
    msg = bot.send_message(msg.chat.id,
                            "...", reply_markup=setMarkup(["Voltar começo"]))
    bot.register_next_step_handler(msg, intro3)

def cashback(msg):
    msg = bot.send_message(msg.chat.id,
                            "Cashback", reply_markup=setMarkup(["Voltar começo"]))
    bot.register_next_step_handler(msg, intro3)

def cupons(msg):
    msg = bot.send_message(msg.chat.id,
                            "Cupons", reply_markup=setMarkup(["Voltar começo"]))
    bot.register_next_step_handler(msg, intro3)

@bot.message_handler(func=lambda msg: (msg.text.lower() == "fim"))
def fim(msg):
    msg = bot.send_message(msg.chat.id,
                               "Atendimento finalizado, caso precise de mais algo basta enviar /start no chat")


@bot.message_handler(func=lambda message: True)
def echo_all(msg):
    bot.reply_to(msg, "Por favor, selecione uma das alternativas exibidas")
    intro(msg)


# bot.reply_to(message, message.text)

# @bot.message_handler(content_types=["video"])  # reconhecendo os parâmetros enviados para o chatbot.
# def tratamento_video(msg):
#     global token
#     id_arquivo = msg.video.file_id
#     arquivo = bot.get_file(id_arquivo)
#     caminho_arquivo = arquivo.file_path
#     downloaded_file = bot.download_file(caminho_arquivo)
#     with open(id_arquivo + 'new_file.mp4', 'wb') as new_file:
#         new_file.write(downloaded_file)
#     bot.reply_to(msg, transcriber(id_arquivo + 'new_file.mp4', id_arquivo + 'new_file.wav'))


# def transcriber(PATHsrc, PATHdst):
#     r = sr.Recognizer()
#     sound = AudioSegment.from_file(PATHsrc)
#     sound.export(PATHdst, format="wav")

#     with sr.AudioFile(PATHdst) as source:
#         audio = r.record(source)

#         try:
#             text = r.recognize_google(audio, language='pt-BR')
#             # text = r.recognize_google(audio)

#             return ("Transcrição do aúdio : {}".format(text))
#         except:
#             return ("Não foi possível transcrever o aúdio!")


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
