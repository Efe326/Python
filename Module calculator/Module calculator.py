import calculator

while True:
    print("1- Toplama")
    print("2- Çıkarma")
    print("3- Çarpma")
    print("4- Bölme")
    print("0- Çıkış")

    secim = input("Yapmak istediğiniz işlemi seçin: ")

    if secim == "0":
        print("Program sonlandırıldı.")
        break

    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))

    if secim == "1":
        sonuc = calculator.Topla(sayi1, sayi2)
        print("Toplam:", sonuc)
    elif secim == "2":
        sonuc = calculator.FarkAl(sayi1, sayi2)
        print("Fark:", sonuc)
    elif secim == "3":
        sonuc = calculator.Carp(sayi1, sayi2)
        print("Çarpım:", sonuc)
    elif secim == "4":
        while sayi2 == 0:
            sayi2 = float(input("İkinci sayı sıfır olamaz, lütfen farklı bir sayı girin: "))
        sonuc = calculator.Bol(sayi1, sayi2)
        print("Bölüm:", sonuc)
    else:
        print("Bir hata oluştu yaw, Lütfen tekrar deneyin.")