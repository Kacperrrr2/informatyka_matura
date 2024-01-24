#lipiec matura
#zadanie 4.1
plik = open('identyfikator_przyklad.txt', 'r')
wiersze = plik.readlines()

# zadanie 4.1
max_suma = 0
max_numery = []

for wiersz in wiersze:
    wiersz=wiersz.strip()
    suma_cyfr = 0
    for i in range(3, len(wiersz)):
        suma_cyfr += int(wiersz[i])

    if suma_cyfr > max_suma:
        max_suma = suma_cyfr
        max_numery.clear()
        max_numery.append(wiersz)
    elif suma_cyfr == max_suma:
        max_numery.append(wiersz)



#zadanie 4.2

palindromy = []
def isPalindrome(s):
    return s == s[::-1]


for wiersz in wiersze:
    wiersz = wiersz.strip()
    if (isPalindrome(wiersz[0]+wiersz[1]+wiersz[2])):
        palindromy.append(wiersz)
    if(isPalindrome(wiersz[3]+wiersz[4]+wiersz[5]+wiersz[6]+wiersz[7]+wiersz[8])):
        palindromy.append(wiersz)





#zadnie 4.3
wartosc=0
sprawdzenie=[]
slownik=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
wagi=[7, 3, 1, 0,7, 3, 1, 7, 3]
cyferki=[10, 11, 12 ,13 ,14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
for wiersz in wiersze:
    wiersz = wiersz.strip()
    for i in range(len(cyferki)):
        if wiersz[0]==slownik[i]:
            sprawdzenie.append(cyferki[i])
    for i in range(len(cyferki)):
        if wiersz[1] == slownik[i]:
            sprawdzenie.append(cyferki[i])
    for i in range(len(cyferki)):
        if wiersz[2] == slownik[i]:
            sprawdzenie.append(cyferki[i])
    for i in range(3, len(wiersz)):
       sprawdzenie.append(int(wiersz[i]))

    for i in range(len(wiersz)):
        if i == 3:
            continue;
        else:
            sprawdzenie[i] = int(sprawdzenie[i]) * wagi[i]

    for i in range(len(wiersz)):
        if i == 3:
            continue;
        else:
           wartosc=wartosc+sprawdzenie[i]

    wartoscpomodulo = wartosc % 10
    if wartoscpomodulo != int(wiersz[3]):
         print(wiersz)
    sprawdzenie.clear()
    wartosc=0





