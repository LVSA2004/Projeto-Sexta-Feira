import pyttsx3
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
from pytube import YouTube
from pytube import Playlist
import moviepy.editor as mp
import re

try:
    microfone = sr.Microphone()
    reconhecedor = sr.Recognizer()
    with microfone as mic:
        reconhecedor.adjust_for_ambient_noise(mic)
        print("Diga algo...")
        robo = pyttsx3.init()
        robo.setProperty('volume', 1.0)
        robo.setProperty('rate', 160)
        robo.runAndWait()
        reconhecedor.adjust_for_ambient_noise(mic)
        audio = reconhecedor.listen(mic)
        print("Reconhecendo...")
        texto = reconhecedor.recognize_google(audio, language='pt')
        print("Você falou: ", texto)

        respostas = ["OK SEXTA-FEIRA", "SEXTA-FEIRA", "FRIDAY", "OK FRIDAY"]
        comando = ["CADASTRAR EVENTO NA AGENDA"]
        comando2 = ["LEIA A AGENDA"]
        comando3 = ["CRIE UM RECADO"]
        comando4 = ["LEIA OS RECADOS"]
        comando5 = ["ABRA O CS"]
        comando6 = ["FAÇA O DOWNLOAD DE UMA MÚSICA"]
        if texto.upper() in respostas:
            print("Sim, mestre. O que posso fazer?")
            robo.say("Sim, mestre. O que posso fazer?”")
            robo.runAndWait()
            audio = reconhecedor.listen(mic)
            print("Reconhecendo...")
            texto = reconhecedor.recognize_google(audio, language='pt')
            print("Você falou: ", texto)
            if texto.upper() in comando:
                # Espera por uma nova entrada de voz para pegar o texto do evento
                print("Qual evento devo cadastrar?")
                robo.say("Qual evento devo cadastrar?")
                robo.runAndWait()
                reconhecedor.adjust_for_ambient_noise(mic)
                audio = reconhecedor.listen(mic)
                evento = reconhecedor.recognize_google(audio, language='pt')
                print("Evento cadastrado: ", evento)
                robo.say("Evento cadastrado: ", evento)
                # Cria um arquivo de texto chamado "agenda.txt" e escreve o evento dentro dele
                with open("agenda.txt", "w") as arquivo:
                    arquivo.write(evento)
            if texto.upper() in comando2:
                # Espera por uma nova entrada de voz para pegar o texto do evento
                print("Aqui estão os eventos agendados: ")
                robo.say("Aqui estão os eventos agendados: ")
                robo.runAndWait()
                arq = open("agenda.txt")
                linhas = arq.readlines()
                for linha in linhas:
                    print(linha)
                    robo.say(linha)
                    robo.runAndWait()
                else:
                    print("Nenhum evento cadastrado na agenda")
            if texto.upper() in comando3:
                # Espera por uma nova entrada de voz para pegar o texto do evento
                print("O que devo guardar no recado?")
                robo.say("O que devo guardar no recado?")
                robo.runAndWait()
                reconhecedor.adjust_for_ambient_noise(mic)
                audio = reconhecedor.listen(mic)
                recado = reconhecedor.recognize_google(audio, language='pt')
                print("Recado cadastrado com sucesso!")
                robo.say("Recado cadastrado com sucesso!")
                tts = gTTS(recado,lang='pt')
                tts.save('recado.mp3')
            if texto.upper() in comando4:
                # Espera por uma nova entrada de voz para pegar o texto do evento
                print("Segue o recado gravado: ")
                robo.say("Segue o recado gravado: ")
                robo.runAndWait()
                os.system('recado.mp3')
            if texto.upper() in comando5:
                # Espera por uma nova entrada de voz para pegar o texto do evento
                print("Abrindo o CS:GO")
                robo.say("Abrindo o CS:GO")
                robo.runAndWait()
                os.system("start steam://rungameid/730")
            if texto.upper() in comando6:
                # Espera por uma nova entrada de voz para pegar o texto do evento
                print("Qual música devo baixar?")
                robo.say("Qual música devo baixar?")
                robo.runAndWait()
                link = input('Digite o Link do Vídeo: ')
                yt = YouTube(link)
                # Fazer o dowload
                ys = yt.streams.filter(only_audio=True)[0]
                ys.download()
                # Converter o video(mp4) para mp3
                print("Download Completo")
            else:
                print("Desculpe, não entendi o comando")
                robo.say("Desculpe, não entendi o comando")
                robo.runAndWait()
        else:
            print("Desculpe, não entendi o comando")
            robo.say("Desculpe, não entendi o comando")
            robo.runAndWait()
except:
    print("Travou aqui pae")