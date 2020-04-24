import numpy as np
N = 33

def alfavit(P):
    for i in range(len(P)):  # каждой букве сопоставляем номер из алфавита (т.е. ё отсутствует в utf добавляем ее вручную)
        if ord(P[i]) > 1071 and ord(P[i]) < 1078:
            P[i] = ord(P[i]) - 1072
        elif ord(P[i]) > 1077 and ord(P[i]) < 1104:
            P[i] = ord(P[i]) - 1071
        elif ord(P[i]) == 1105:
            P[i] = 6
        elif ord(P[i]) < 1071:
            P[i] = ord(P[i]) - 96
    return (P)

def shifr():
    try:
        print("Введите слово")
        P = list(input().lower())
        print("Введите ключ")
        K = list(input().lower())
        D = []
        while len(K) < len(P):
            i=0
            D.append(K[i])
            K.append(D[i])
            i = i + 1

        return alfavit(P),alfavit(K)
    except Exception:
        print("Ошибка")
        shifr()

P, K = shifr()
print("Открытое сообщение",P)
print("Ключ",K)

C = []
for i in range(len(P)):
    C.append((P[i] + K[i])%N)

print("Зашифрованное сообщение",C)