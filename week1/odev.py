"""Soru 1"""
"""
Bir metnin uzunluğunu hesaplamak için bir Python programı yazınız. ipucu Len fonksiyonu
"""

# text=input("Lütfen metni giriniz: ")
# print("Metnin uzunluğu boşluklar dahil "+str(len(text))+" karakter.")
# print("Metnin uzunluğu boşluklar haric "+str(len(text.replace(" ","")))+" karakter.")

####################################
"""Soru 2"""
"""Kullanıcı tarafından girilen bir metnin ilk iki ve son iki karakterini ekrana yazdıran Python programını yazınız."""

# text=input("Lütfen metni giriniz: ")
# print(text[:2] +' '+text[-2:])

####################################
"""Soru 3"""
"""Kullanıcıdan değişecek metin ve eski harf ve yeni harf bilgisini alarak girilen metin üzerinden değişikliği yapıp sonucu ekrana yazdıran Python programını yazınız."""

# text=input("Lütfen değişecek metni giriniz: ")
# oldChar,newChar=input("Lütfen sırasıyla değişmesini istediğiniz karakterleri 'eski ve yeni' sırası ile giriniz: ").split()
# print(text.replace(oldChar,newChar))

####################################
"""Soru 4"""
"""Kullanıcı tarafından girilen bir kelimenin palindrom olup olmadığını karşılaştırma operatöründen faydalanarak print() fonksiyonu ile ekrana yazdırınız. """

# palindrom = input("Lütfen kelime giriniz: ")
# print("Palindrom" if palindrom[0::]==palindrom[::-1] else "Palindrom değil")

####################################
"""Soru 5"""
"""Girilen bir metnin son 2 karakterini 4 defa çoğaltarak ekrana yazan Python programını yazınız. `*` aritmetik operatöründen faydalanabilirsiniz. """

# text=input("Lütfen metin giriniz: ")
# print(text[-2:]*4)


####################################
"""Soru 6"""
"""
5 elemanlı bir liste oluşturunuz. Bu liste içerisindeki 2. elemanı 100 ile değiştiren python kodu yazınız.
"""
# liste = ["a",2,4,"c",5]
# liste[1]=100
# print(liste)

####################################
"""Soru 6"""
"""İki farklı listede tutulan verileri tek bir listede sırasıyla append,extend metodlarıyla ve "+" operatörü ile birleştiren python kodunu yazınız 
liste1 = [1,2,3]
liste2 = [4,5,6]
liste3 = ?????
"""
# liste1 = [1,2,3]
# liste2 = [4,5,6]
# for i in liste2: liste1.append(i)
# liste3 = liste1
# print(liste3)

# liste1.extend(liste2)
# liste3 = liste1
# print(liste3)

# liste3 =liste1+liste2
# print(liste3)

####################################
"""Soru 7"""
"""Oluşturduğunuz 3 elemanlı bir liste içerisine ilk sıraya "Elma" kelimesini ekleyiniz. """

# liste1 = [1,2,3]
# liste1.insert(0,"Elma")
# print(liste1)

####################################
"""Soru 8"""
"""liste = [1,2,3,4,5,6,7,1,3,3,3,2,2,1,23]
yukarıdaki listeden ilk 3 sayısını silip ekrana yazdırınız. 
"""

# liste = [1,2,3,4,5,6,7,1,3,3,3,2,2,1,23]
# del liste[:3]
# print(liste)


####################################
"""Soru 9"""
"""
liste1 = ["1",1,2,"3"]
Yukarıdaki listenin bir kopyasını alarak 250 sayısını listenin sonuna ekleyiniz,her iki listeyi ekrana yazdırınız.
Beklenen Çıktı:
["1",1,2,"3"] => Liste1 Çıktısı
["1",1,2,"3",250] => Liste2 Çıktısı
"""

# liste1 = ["1",1,2,"3"]
# liste2 = liste1.copy()
# liste2.append(250)
# print(liste1)
# print(liste2)

####################################
"""Soru 9"""
"""
Aşağıdaki üç farklı sözlüğü tek sözlükte birleştiren python kodunu yazınız
dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50,6:60}
Beklenen Çıktı : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
# dict1={1:10, 2:20}
# dict2={3:30, 4:40}
# dict3={5:50,6:60}
# dict1.update(dict2)
# dict1.update(dict3)
# dict4 = dict1
# print(dict4)
# dict5 = {**dict1, **dict2, **dict3}
# print(dict5)

####################################
"""Soru 9"""
"""sozluk ={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
Sözlükteki en son elemanı silerek ekrana işlem sonucunu yazdırınız
Beklenen Çıktı :(6,60)
"""

# sozluk ={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# sozluk.popitem()
# print(sozluk)
# sozluk ={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# del sozluk[6]
# print(sozluk)

####################################
"""Soru 10"""
"""dict1={1:10, 2:20}
Yukarıdaki sözlüğe bir eleman ekleyiniz. 
Beklenen Çıktı :{1:10, 2:20, 3:30}
"""
# dict1={1:10, 2:20}
# dict1[3] =30
# print(dict1)

####################################
"""Soru 11"""
"""liste=[1,2,3,4,5]
    a.Yukarıdaki listeden faydalanarak bir sözlük oluşturun 
    b.sözlüğün her alamanının karşılığına değer olarak anahtarda bulunan sayısal değerin 10 katını eşitleyin.
Beklenen Çıktı :
a. {1:0,2:0,3:0,4:0,5:0}
b. {1:10,2:20,3:30,4:40,5:50}
"""
# liste=[1,2,3,4,5]
# dict1 = {liste[i]: 0 for i in range(0, len(liste))}
# print(dict1)
# dict1.update((i, (j+1)*(10*(i))) for i,j in dict1.items())
# print(dict1)


####################################
"""Soru 12"""
"""sozluk={1:10,2:20,3:30,4:40,5:50}
Sözlük içerisine 6 sayısını anahtar olarak değeri 60 olacak şekilde setdefault fonksiyonunu kullanarak ekleyiniz

"""
# sozluk={1:10,2:20,3:30,4:40,5:50}
# sozluk.setdefault(6, 60)
# print(sozluk)


####################################
"""Soru 13"""
"""
Seven Segment Display 
https://en.wikipedia.org/wiki/Seven-segment_display

* * * * *
*       *
*       *
* * * * *
*       *
*       *
* * * * *

8 sayısı girildiğinde yukarıdaki çıktıyı veren python programını 0 dan 9 a kadar olan sayılar için yazalım
## hex,bin,zfill, tek satırda if

"""

#Maalesef stackoverflowdan :(
# representations = {
#     '0': ('***', '* *', '* *', '* *', '***'),
#     '1': ('  *', '  *', '  *', '  *', '  *'),
#     '2': ('***', '  *', '***', '*  ', '***'),
#     '3': ('***', '  *', '***', '  *', '***'),
#     '4': ('* *', '* *', '***', '  *', '  *'),
#     '5': ('***', '*  ', '***', '  *', '***'),
#     '6': ('***', '*  ', '***', '* *', '***'),
#     '7': ('***', '  *', '  *', '  *', '  *'),
#     '8': ('***', '* *', '***', '* *', '***'),
#     '9': ('***', '* *', '***', '  *', '***'),
#     '.': ('   ', '   ', '   ', '   ', '  *'),
# }

# def seven_segment(number):
#     digits = [representations[digit] for digit in str(number)]
#     for i in range(5):
#         print("  ".join(segment[i] for segment in digits))

# seven_segment(23)

####################################
"""Soru 14"""
"""
Bir listeyi bir sözlükte sıralamak için bir Python programı yazın <br>
Örnek Veri: num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
"""
# num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# newDict = sorted(num.items())
# for key, value in newDict:
#     value.sort()
# print(newDict)


####################################
"""Soru 15"""
"""sozluk = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']} 

ilgili sözlükten anahtar kısımlarında bulunan boşlukları temizleyen python kodu yazınız. 
"""

# sozluk = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']} 
# sozluk = {i.replace(' ', ''): j for i, j in sozluk.items()}
# print(sozluk)

####################################
"""Soru 16"""
"""
liste1=[1,2,3]
liste2=[4,5,6,7,8]
iki listeyi liste3 ile birleştiriniz?
"""
# liste1=[1,2,3]
# liste2=[4,5,6,7,8]
# liste3=[9,10]   #liste 3 dolu ise
# liste3.extend(liste1+liste2)
# liste3.sort()
# liste3 = liste1+liste2   #liste 3 boş ise
# print(liste3)

####################################
"""Soru 17"""
"""liste=[1,2,3,4,5,6] listesindeki 1. elemanı del komutu ile siliniz?

"""
# liste=[1,2,3,4,5,6]
# del liste[0]
# print(liste)

####################################
"""Soru 18"""
"""
liste=["elma" , "armut", "çilek"] listesine append komutu ile sona 3 elemanını ekleyiniz?
"""

# liste=["elma" , "armut", "çilek"]
# liste.append(3)
# print(liste)

####################################
"""Soru 18"""
"""Girilen on sayı içerisinden en büyük üç sayıyı bulmak için bir Python fonksiyonu yazınız"""

# def enBuyukSayi():
#     print("Lütfen 10 tane sayı giriniz")
#     liste =[]
#     for i in range(10):
#         sayi = int(input("Sayi "))
#         liste.append(sayi)
#         max_sayi = max(liste)
#     print(max_sayi)

# enBuyukSayi()

####################################
"""Soru 19"""
"""Bir metin içerisindeki büyük ve küçük harflerin listesini yazdıran python programını yazınız."""

# text = input("Lütfen bir metin giriniz: ")
# listeKucuk=[]
# listeBuyuk=[]
# for i in range(len(text)):
#     if text[i].isupper(): listeKucuk.append(text[i])
#     elif text[i]== ' ':continue
#     else: listeBuyuk.append(text[i])
# print(listeKucuk)
# print(listeBuyuk)

####################################
"""Soru 20"""
"""kullanıcıdan alınan 10 sayının çift ve tek sayıların sayısını ekrana yazdıran programı yazınız. """
# def ciftMiTekMi():
#     print("Lütfen 10 tane sayı giriniz")
#     listeCift =[]
#     listeTek =[]
#     for i in range(10):
#         sayi = int(input("Sayi "))
#         if sayi % 2 == 0 : listeCift.append(sayi)
#         else:  listeTek.append(sayi)
#     print("Çift Sayılar: ", listeCift)
#     print("Tek Sayılar: ", listeTek)

# ciftMiTekMi()

