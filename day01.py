
#Stringlerle Çalışma

print("selam")              #Ekrana mesaj yazdırma
mesaj="selam"               #Değişkene veri atama

print(mesaj.upper())        #Tüm harfler büyük
print(mesaj.lower())        #Tüm harfler küçük
print(mesaj.capitalize())   #İlk harf büyük
print(mesaj[::-1].capitalize()) #Tersten yazdırma ve ilk harf büyük
print(mesaj[1:3])           #index1 den 3. indexe kadar olan kısmı yazdırma(aradaki fark kadar harf basar)
print(mesaj*10)             #Ekrana belirtilen sayı kadar ifade yazdırma
ad="Ali"
yas="20"
print("{} , {} yaşındadır".format(ad,yas))  # String formatlama
print(f"{ad}, {yas} yasındadır...")         # String formatlama

i="Ali"

print(i)