import sys

işlem=True
while True:
    anapara=int(input("Ana para miktarını giriniz;"))
    faiz=float (input("Faizmiktarını giriniz; "))
    ay=int(input("Lütfen süreyi ay olarak giriniz; "))
    faizlipara = anapara + (anapara*faiz*ay/1200)
    print(f"Ana paranız; {anapara} TL\nFaizli paranız; {faizlipara}\nFaizden kazanılan tutar; {faizlipara-anapara}")

    if type (anapara) and type(faiz) and type(ay) != int:
        print("Lütfen sadece sayı giriniz")

    çıkış =input("Tekrar hesap yapmak için 'R'ye çıkmak için Q'ye basınız ").lower()
    if çıkış == "r":
        işlem == True
    elif çıkış == "q":
        sys.exit("Tekrar bekleriz!")
    else:
        print("lütfen anlamlı bir komut giriniz")


