def hesap_makinesi():
    print("Basit Hesap Maknesi")
    print("Toplama (+), Çıkarma (-), Çarpma (*), Bölme (/)")
    
    sayi1 = float(input("Birinci sayıyı gir: "))
    islem = input("Yapmak istediğin işlem (+ - * /): ")
    sayi2 = float(input("İkinci sayıyı gir: "))

    if islem == "+":
        sonuc = sayi1 + sayi2
    elif islem == "-":
        sonuc = sayi1 - sayi2
    elif islem == "*":
        sonuc = sayi1 * sayi2
    elif islem == "/":
        if sayi2 != 0:
            sonuc = sayi1 / sayi2
        else:
            return "Hata: 0'a bölünemez."
    else:
        return "Geçersiz işlem amk"

    return f"Sonuç: {sonuc}"

print(hesap_makinesi())
