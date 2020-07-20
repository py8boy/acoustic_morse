import winsound                                     # importei a biblioteca winsound para emitir os sons
from time import sleep                              # importei a função sleep para gerenciar os intervalos entre os sons


def dit():                                         # sub-rotina para emitir os sons equivalentes ao dit (.)
    frequence = 1500
    alarmTime = 150
    winsound.Beep(frequence, alarmTime)


def dah():                                         # sub-rotina para emitir os sons equivalentes ao dah (-)
    frequence = 1500
    alarmTime = 1500
    winsound.Beep(frequence, alarmTime)


def breaks():                                       # 'regulamenta' os intervalos entre as palavras
    sleep(5)



def verifyMsg(msg):                                             # adiciona a mensagem convertida na lista convertData
    for char in msg:
        convertedData.append(general[char])


def soundMsg(msg_list):                                 # emite os sons respectivos ao sinais (. e -)
    for char in msg_list:
        print(char)
        sleep(1)
        if (char == ' '):
            breaks()
        for element in char:
            if (element == '.'):
                dit()
            elif (element == '-'):
                dah()


def cleaningData(dataList):
    dataList.clear()


def callFunctions():
    verifyMsg(userMsg)
    soundMsg(convertedData)
    cleaningData(convertedData)



general = {'a': '.-', 'b': '-...',
           'c': '-.-.', 'd': '-..',
           'e': '.', 'f': '..-.',
           'g': '--.', 'h': '....',
           'i': '..', 'j': '.---',
           'k': '-.-', 'l': '.-..',
           'm': '--', 'n': '-.',
           'o': '---', 'p': '.--.',
           'q': '--.-', 'r': '.-.',
           's': '...', 't': '-',
           'u': '..-', 'v': '...-',
           'w': '.--', 'x': '-..-',
           'y': '-.--', 'z': '--..',
           '1': '.----', '2': '..---',
           '3': '...--', '4': '....-',
           '5': '.....', '6': '-....',
           '7': '--...', '8': '---..',
           '9': '----.', '10': '-----', 
           ' ': ' ', '.': '.-.-.-',
           ',': '--..--', '?': '..--..'}

convertedData = []

while (True):
    try:
        print('\n \033[32m Do not type accents, exclamation marks or symbols \033[m')
        userMsg = input(str('Enter your message: ')).lower()
        callFunctions()

    except KeyError:
        print('\033[31m Invalid text, please type your text again \033[m')

