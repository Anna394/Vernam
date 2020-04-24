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
        if ord(P[0])>1000:
            language = True
        else:
            language = False

        print("Введите ключ")
        K = list(input().lower())
        D = []
        while len(K) < len(P):
            i=0
            D.append(K[i])
            K.append(D[i])
            i = i + 1

        return alfavit(P),alfavit(K), language
    except Exception:
        print("Ошибка")
        shifr()

P, K, language = shifr()
print("Зашифрованное сообщение",P)
print("Ключ",K)

C = []
for i in range(len(P)):
    C.append((P[i]+N-K[i])%N)

print("Зашифрованное сообщение",)

for i in range(len(C)):
    if language== True:
        if C[i]>=0 and C[i]<=6:
            C[i] = chr(C[i]+1072)
        elif C[i] >= 7 and C[i] <= 32:
            C[i] = chr(C[i] + 1071)
    else:
        C[i] = chr(C[i] + 96)
print(C)