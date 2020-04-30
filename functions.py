import telebot
import time
from pydub import AudioSegment
import speech_recognition as sr


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
            return ("Impossibruuuu")

def setMarkup(q, opt): #q para question ou pergunta, e opt é uma lista de strings com as opções
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	itembtnY = types.KeyboardButton(opt[0])
	itembtnN = types.KeyboardButton(opt[1])
	return(markup.row(itembtnY, itembtnN))
