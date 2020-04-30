from telebot import types
import telebot
import time
from pydub import AudioSegment
import speech_recognition as sr

# token = "733315422:AAH8LFFOYXe0saMXY4Z7txYKF3Qu7IOlvu4" #HAL
token = "705662565:AAFft7WvsCJDp8Kim0irVAFhMQERXN6nAqE"  # VIUW

bot = telebot.TeleBot(token)
respostas = list()


def setMarkup(opt):  # opt é uma lista de strings com as opções
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    itembtnY = types.KeyboardButton(opt[0])
    itembtnN = types.KeyboardButton(opt[1])
    return (markup.row(itembtnY, itembtnN))


@bot.message_handler(commands=["start"])
def send_welcome(msg):
    # bot.reply_to(msg, "Clique no botão para iniciar seu processo de subscrição.")
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    itembtn = types.KeyboardButton("Iniciar")
    bot.send_message(msg.chat.id, "Clique no botão para iniciar seu processo de subscrição.",
                     reply_markup=markup.row(itembtn))


@bot.message_handler(func=lambda msg: (msg.text == "Iniciar"))
def nome(msg):
    # markup = types.ReplyKeyboardRemove(selective=False)
    # tb.send_message(chat_id, message, reply_markup=markup)
    # message=bot.send_message(msg.chat.id, "Choose one letter:", reply_markup=markup, one_time_keyboard=True)
    message = bot.send_message(msg.chat.id, "Qual é o seu nome completo?")
    bot.register_next_step_handler(message, peso)


def peso(msg):
    message = bot.send_message(msg.chat.id, "Qual o seu peso?")
    bot.register_next_step_handler(message, altura)


def altura(msg):
    message = bot.send_message(msg.chat.id, "Qual a sua altura")
    bot.register_next_step_handler(message, fumante1)


def fumante1(msg):
    message = bot.send_message(msg.chat.id, "O(a) senhor fumou ou fuma cigarro, charuto, cachimbo e/ou outros?",
                               reply_markup=setMarkup(["Sim", "Não"]))
    bot.register_next_step_handler(message, fumante2)


def fumante2(msg):
    if msg.text == "Sim":
        message = bot.send_message(msg.chat.id, "Por favor, especifique quais. Informe a frequência e quantidade.")
        bot.register_next_step_handler(message, alcool1)
    elif msg.text == 'Não':
        alcool1(msg)


def alcool1(msg):
    message = bot.send_message(msg.chat.id, "O(A) senhor(a) faz uso de álcool?", reply_markup=setMarkup(["Sim", "Não"]))
    bot.register_next_step_handler(message, alcool2)


def alcool2(msg):
    if msg.text == "Sim":
        message = bot.send_message(msg.chat.id, "Por favor, especifique quais. Informe a frequência e quantidade.")
        bot.register_next_step_handler(message, pressao)
    elif msg.text == "Não":
        pressao(msg)


def pressao(msg):
    message = bot.send_message(msg.chat.id, "O(A) senhor(a) sabe o valor da sua pressão arterial?")
    bot.register_next_step_handler(message, hipertensao)


def hipertensao(msg):
    message = bot.send_message(msg.chat.id, "O(A) senhor(a) tem ou teve hipertensão arterial?",
                               reply_markup=setMarkup(["Sim", "Não"]))
    bot.register_next_step_handler(message, glicose)


def glicose(msg):
    message = bot.send_message(msg.chat.id,
                               "O(A) senhor(a) teve ou tem alguma alteração no nível de glicose ou diabetes?",
                               reply_markup=setMarkup(["Sim", "Não"]))
    bot.register_next_step_handler(message, asma)


def asma(msg):
    message = bot.send_message(msg.chat.id,
                               "O(A) senhor(a) sofre ou já sofreu de transtornos ou alterações do aparelho respiratório, tais como Asma, Bronquite Crônica, Enfisema, Tuberculose ou qualquer outro transtorno não mencionado?",
                               reply_markup=setMarkup(["Sim", "Não"]))
    bot.register_next_step_handler(message, tumor1)


def tumor1(msg):
    message = bot.send_message(msg.chat.id,
                               "O(A) senhor(a) apresenta ou apresentou algum tumor benigno ou maligno e ou especificamente Linfoma e/ou Leucemia?",
                               reply_markup=setMarkup(["Sim", "Não"]))
    bot.register_next_step_handler(message, tumor2)


def tumor2(msg):
    if msg.text == "Sim":
        message = bot.send_message(msg.chat.id, "Por favor, especifique quais. Informe a frequência e quantidade.")
        bot.register_next_step_handler(message, cardio1)
    elif msg.text == "Não":
        cardio1(msg)


def cardio1(msg):
    message = bot.send_message(msg.chat.id,
                               "Nos últimos 5 anos, o(a) senhor(a) apresentou dificuldade de respirar, dor ou pressão no peito?",
                               reply_markup=setMarkup(["Sim", "Não"]))
    bot.register_next_step_handler(message, cardio2)


def cardio2(msg):
    if msg.text == "Sim":
        message = bot.send_message(msg.chat.id, "Por favor, especifique descreva o caso e informe a última ocorrência")
        bot.register_next_step_handler(message, AVC1)
    elif msg.text == "Não":
        AVC1(msg)


def AVC1(msg):
    message = bot.send_message(msg.chat.id,
                               "O(A) senhor(a) tem ou teve algum transtorno ou alteração cerebrovasculares, tais como algum tipo de paralisia, AVC e/ou outros?",
                               reply_markup=setMarkup(["Sim", "Não"]))
    bot.register_next_step_handler(message, AVC2)


def AVC2(msg):
    if msg.text == "Sim":
        message = bot.send_message(msg.chat.id, "Por favor, especifique descreva o caso e informe a última ocorrência")
        bot.register_next_step_handler(message, hospital1)
    elif msg.text == "Não":
        hospital1(msg)


def hospital1(msg):
    message = bot.send_message(msg.chat.id, "O(A) senhor(a) já esteve hospitalizado?",
                               reply_markup=setMarkup(["Sim", "Não"]))
    bot.register_next_step_handler(message, hospital2)


def hospital2(msg):
    if msg.text == "Sim":
        message = bot.send_message(msg.chat.id, "Por favor, especifique descreva o caso e informe a última ocorrência")
        bot.register_next_step_handler(message, med1)
    elif msg.text == ("Não"):
        med1(msg)


def med1(msg):
    message = bot.send_message(msg.chat.id, "O(A) senhor(a) faz uso de medicação contínua?",
                               reply_markup=setMarkup(["Sim", "Não"]))
    bot.register_next_step_handler(message, med2)


def med2(msg):
    if msg.text == "Sim":
        message = bot.send_message(msg.chat.id, "Por favor, especifique a medicação.")
        bot.register_next_step_handler(message, historico1)
    elif msg.text == "Não":
        historico1(msg)


def historico1(msg):
    message = bot.send_message(msg.chat.id,
                               "O(A) senhor(a) tem um histórico familiar de Hipertensão, Infarto do miocárdio, AVC, Obesidade, Diabetes, Câncer do Colón, Câncer de Próstata, Câncer de Mama ou de Ovário?",
                               reply_markup=setMarkup(["Sim", "Não"]))
    bot.register_next_step_handler(message, historico2)


def historico2(msg):
    if msg.text == "Sim":
        message = bot.send_message(msg.chat.id, "Por favor, especifique a doença e o grau de parentesco")
        bot.register_next_step_handler(message, ativfisica1)
    elif msg.text == "Não":
        ativfisica1(msg)


def ativfisica1(msg):
    message = bot.send_message(msg.chat.id, "O(A) senhor(a) pratica atividades físicas?",
                               reply_markup=setMarkup(["Sim", "Não"]))
    bot.register_next_step_handler(message, ativfisica2)


def ativfisica2(msg):
    if msg.text == "Sim":
        message = bot.send_message(msg.chat.id, "Se sim, qual e em que frequência?")
        bot.register_next_step_handler(message, fim)
    elif msg == "Não":
        fim(msg)


def fim(msg):
    message = bot.send_message(msg.chat.id,
                               "Sua video entrevista está encerrada, em breve você receberá contato com o resultado de sua subscrição")


# @bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Por favor, responda com Sim ou Não")


# bot.reply_to(message, message.text)

@bot.message_handler(content_types=["video"])  # reconhecendo os parâmetros enviados para o chatbot.
def tratamento_video(msg):
    global token
    id_arquivo = msg.video.file_id
    arquivo = bot.get_file(id_arquivo)
    caminho_arquivo = arquivo.file_path
    downloaded_file = bot.download_file(caminho_arquivo)
    with open(id_arquivo + 'new_file.mp4', 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(msg, transcriber(id_arquivo + 'new_file.mp4', id_arquivo + 'new_file.wav'))


def transcriber(PATHsrc, PATHdst):
    r = sr.Recognizer()
    sound = AudioSegment.from_file(PATHsrc)
    sound.export(PATHdst, format="wav")

    with sr.AudioFile(PATHdst) as source:
        audio = r.record(source)

        try:
            text = r.recognize_google(audio, language='pt-BR')
            # text = r.recognize_google(audio)

            return ("Transcrição do aúdio : {}".format(text))
        except:
            return ("Não foi possível transcrever o aúdio!")


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
