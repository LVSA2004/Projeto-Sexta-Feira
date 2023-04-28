import os
import sys
import pyttsx3
import speech_recognition as sr
import translate
from gtts import gTTS
from playsound import playsound
import pyautogui as pyg
from time import sleep
from bs4 import BeautifulSoup
from requests import get


def ErroComando():
    print("Desculpe, não entendi o comando")
    robo.say("Desculpe, não entendi o comando")
    robo.runAndWait()


def CadastrarEvento():
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


def LerAgenda():
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


def CriarRecado():
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


def LerRecado():
    # Espera por uma nova entrada de voz para pegar o texto do evento
    print("Segue o recado gravado: ")
    robo.say("Segue o recado gravado: ")
    robo.runAndWait()
    os.system('recado.mp3')


def AbrirCS():
    # Espera por uma nova entrada de voz para pegar o texto do evento
    print("Abrindo o CS:GO")
    robo.say("Abrindo o CS:GO")
    robo.runAndWait()
    os.system("start steam://rungameid/730")


def PesquisarGoogle():
    # Espera por uma nova entrada de voz para pegar o texto do evento
    print("O que  devo pesquisar?")
    robo.say("O que  devo pesquisar?")
    robo.runAndWait()
    pesquisa = pyg.prompt('O que você deseja pesquisar no Google?')
    while pesquisa == '':
        pyg.alert('Por favor, insira algum texto!')
        pesquisa = pyg.prompt('O que você deseja pesquisar no Google?')
    if texto == None:
        exit()
    pyg.press('win')
    pyg.write('google', interval=0.5)
    pyg.press('Enter')
    sleep(5)
    pyg.write(pesquisa, interval=0.5)
    pyg.press('Enter')


def Noticias():
    print("Segue as notícias mais recentes")
    robo.say("Segue as notícias mais recentes")
    robo.runAndWait()
    site = get('https://news.google.com/news/rss?ned=pt_br&gl=BR&hl=pt')
    noticias = BeautifulSoup(site.text, 'html.parser')
    for item in noticias.findAll('item')[:5]:
        print(item.title.text)
        robo.say(item.title.text)


def Cotacao(moeda):
    requisicao = get(f'https://economia.awesomeapi.com.br/all/{moeda}-BRL')
    cotacao = requisicao.json()
    nome = cotacao[moeda]['name']
    data = cotacao[moeda]['create_date']
    valor = cotacao[moeda]['bid']
    robo.say(f"Cotação do {nome} em {data} é {valor}")



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
        comando6 = ["PESQUISAR NO GOOGLE"]
        comando7 = ["ME MOSTRE AS NOTÍCIAS"]
        comando8 = ["QUAL A COTAÇÃO DO DÓLAR"]
        comando9 = [""]
        comando10 = [""]
        comando11 = [""]
        comando12 = [""]
        comando13 = [""]
        if texto.upper() in respostas:
            print("Sim, mestre. O que posso fazer?")
            robo.say("Sim, mestre. O que posso fazer?”")
            robo.runAndWait()
            audio = reconhecedor.listen(mic)
            print("Reconhecendo...")
            texto = reconhecedor.recognize_google(audio, language='pt')
            print("Você falou: ", texto)
            if texto.upper() in comando:
                CadastrarEvento()
            if texto.upper() in comando2:
                LerAgenda()
            if texto.upper() in comando3:
                CriarRecado()
            if texto.upper() in comando4:
                LerRecado()
            if texto.upper() in comando5:
                AbrirCS()
            if texto.upper() in comando6:
                PesquisarGoogle()
            if texto.upper() in comando7:
                Noticias()
            if texto.upper() in comando8:
                Cotacao()
            if texto.upper() in comando9:
                PesquisarGoogle()
            if texto.upper() in comando10:
                PesquisarGoogle()
            if texto.upper() in comando11:
                PesquisarGoogle()
            else:
                ErroComando()
        else:
            ErroComando()
except:
    print("Travou aqui")