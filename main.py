

import string

def metni_kucult(dil, metin):
    if all(char.islower() for char in metin):
        print("Metin zaten küçük harflerden oluşuyor:", metin)
    else:
        print("Küçültülmüş Metin:", metin.lower())

def metinde_kac_kucuk_kac_buyuk_harf_var(dil, metin):
    kucuk_harf_sayisi = sum(1 for harf in metin if harf.islower())
    buyuk_harf_sayisi = sum(1 for harf in metin if harf.isupper())
    noktalama_sayisi = sum(1 for harf in metin if harf in string.punctuation)
    bosluk_sayisi = sum(1 for harf in metin if harf == ' ')
    print("Metinde {} küçük harf, {} büyük harf, {} noktalama işareti ve {} boşluk bulunmaktadır.".format(
        kucuk_harf_sayisi, buyuk_harf_sayisi, noktalama_sayisi, bosluk_sayisi))

def sirala_harfler(metin):
    alfabe = sorted(set(filter(str.isalpha, metin)))
    siralanmis_metin = ''.join(alfabe)
    return siralanmis_metin

def metindeki_kelime_sayisi(dil, metin):
    kelime_sayisi = len(metin.split())
    print("Metinde toplam {} kelime bulunmaktadır.".format(kelime_sayisi))

def harf_frekanasi_analizi_ve_yazdir(dil, metin):
    alfabeler = {
        "İngilizce": "abcdefghijklmnopqrstuvwxyz",
        "Türkçe": "abcçdefgğhıijklmnoöprsştuüvyz",
        "Almanca": "abcdefghijklmnopqrstuvwxyzäöüß"
    }

    alfabe = alfabeler.get(dil)
    if not alfabe:
        raise ValueError("Desteklenmeyen dil seçildi.")

    harf_sayilari = {harf: 0 for harf in alfabe}
    toplam_harf = 0

    for harf in metin.lower():
        if harf in alfabe:
            harf_sayilari[harf] += 1
            toplam_harf += 1

    if toplam_harf == 0:
        print("Metin, analiz için uygun harfler içermiyor.")
        return

    print("Harf frekansları:")
    for harf, sayi in sorted(harf_sayilari.items(), key=lambda item: item[1], reverse=True):
        yuzde = (sayi / toplam_harf) * 100
        if yuzde > 0:
            print("  {}: %{} ({:.0f} kez)".format(harf, yuzde, sayi))


def metni_ters_cevir(dil, metin):
    ters_metin = metin[::-1]
    print("Ters Çevrilmiş Metin:", ters_metin)


def kisisel_bilgilerimi_yazdir():
    ad = "Yusuf"
    soyad = "Kurt"
    ogrenci_numarasi = "211220053"
    kisisel_not = "Konya teknik üniversitesi selçuktan daha iyi :)"

    print("Adım: " + ad)
    print("Soyadım: " + soyad)
    print("Öğrenci Numaram: " + ogrenci_numarasi)
    print(kisisel_not)

kisisel_bilgilerimi_yazdir()

metin = input("Lütfen bir metin girin: ")
harf_frekanasi_analizi_ve_yazdir(dil="Türkçe", metin=metin)
metni_kucult(dil="Türkçe", metin=metin)
metinde_kac_kucuk_kac_buyuk_harf_var(dil="Türkçe", metin=metin)
metindeki_kelime_sayisi(dil="Türkçe", metin=metin)
metni_ters_cevir(dil="Türkçe", metin=metin)

siralanmis_metin = sirala_harfler(metin)
print("Metindeki harfler alfabetik sırayla sıralanmış hali:", siralanmis_metin)
