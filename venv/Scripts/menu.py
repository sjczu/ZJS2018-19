import numpy as np

def numerInput(komunikat):
    while True:
        try:
            num = float(input(komunikat))
            break
        except ValueError:
            pass
    return num

def menuPrint(opcje):
    for i in range(len(opcje)):
        print('{:d}. {:s}'.format(i+1, opcje[i]))
    wybor = 0
    while not(np.any(wybor == np.arange(len(opcje))+1)):
        wybor = numerInput("Wybierz opcje: ")

    return wybor
