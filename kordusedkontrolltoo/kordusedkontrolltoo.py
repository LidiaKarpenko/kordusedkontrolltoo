#1 
print("sisestage arv: ")
arv = ['(\_/)  ',
       '(o o)  ',
       '/ | \  ']
n = int(input(" "))

for i in arv:
    print(i * n)

#3
from random import randint
n = randint(0, 100)
i = 0
print("sisestage arv vahemikus 1 kuni 100: ")
while True:
    a = int(input())
    if a == n:
        print("te võitsite!")
        break
    if a < n:
        print("peidetuv arv on suurem")
    if a > n:
        print("peidetuv arv on väiksem")
    if a > 100:
        print("sisestage arv, mis on väiksem kui 100")
        break
    i += 1
    if i == 10:
        print(f"te kaotsite. peidetuv arv on {n}")
        break

#4
n1 = int(input("sisestage täis arv: "))
n2 = 0
while n1 > 0:
    digit = n1 % 10
    n1 = n1 // 10
    n2 = n2 * 10
    n2 = n2 + digit  
print("ümberööratud arv on: ",n2)

#5
print("sisestage täis arv: ")
n = int(input())
summa = 0
korrut = 1
while n > 0:
    digit = n % 10
    summa = summa + digit
    korrut = korrut * digit
    n = n // 10
    
print("summa: ", summa)
print("korrutis: ", korrut)





