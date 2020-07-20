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
