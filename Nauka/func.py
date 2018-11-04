import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'To pewne'
    elif answerNumber == 2:
        return 'Zdecydowanie tak'
    elif answerNumber == 3:
        return 'Tak'
    elif answerNumber == 4:
        return 'Niejasna odpowiedź'
    elif answerNumber == 5:
        return 'Zaptaj ponowni później'
    elif answerNumber == 6:
        return 'skoncentruj się'
    elif answerNumber == 7:
        return 'Moja odpowiedź brzmi NIE'
    elif answerNumber == 8:
        return 'To nie wygląda zbyt dobrze'
    elif answerNumber == 9:
        return 'Bardzo wątpliwe'

print(getAnswer(random.randint(1,9)))
