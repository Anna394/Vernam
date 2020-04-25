
import numpy as np

def alfavit(P):
    for i in range(len(P)):  # каждой букве сопоставляем номер из алфавита (т.е. ё отсутствует в utf добавляем ее вручную)
        P[i] = ord(P[i].encode('cp1251'))
    return (P)

def shifr():
    try:
        print("Введите слово")
        P = list(input())
        print("Введите ключ")
        K = list(input())
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
    C.append((P[i] ^ K[i]))

print("Зашифрованное сообщение",C)

for i in range(len(C)):
    print(chr(C[i]).encode('cp1251'))