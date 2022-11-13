import random

secenek = ["taş", "kağıt", "makas"]
tas = secenek[0]
kagit = secenek[1]
makas = secenek[2]
bilgisayarSkor = 0
benimSkor = 0

print("******TAŞ, KAĞIT, MAKAS OYUNUNA HOŞGELDİN!******")
while True:
    
    bilgisayarSecim = random.choice(secenek) # Bilgisayar taş, kağıt ve makas seçeneklerinden rastgele 1 tanesini seçer
    benimSecim = input("\nTaş mı, kağıt mı, makas mı ?: ")
    
    #Taş seçtiğimiz durumlar
    if benimSecim == tas:

        if bilgisayarSecim == tas:
            print("Sonuç: Berabere. Sen: Taş, Bilgisayar: Taş")
            
        elif bilgisayarSecim == kagit:
            print("Sonuç: Bilgisayar Galip. Sen: Taş, Bilgisayar: Kağıt")
            bilgisayarSkor += 1
            
        elif bilgisayarSecim == makas:
            print("Sonuç: Galipsin. Sen: Taş, Bilgisayar: Makas")
            benimSkor += 1
    
    #Kağıt seçtiğimiz durumlar
    if benimSecim == kagit:

        if bilgisayarSecim == tas:
            print("Sonuç: Galipsin. Sen: Kağıt, Bilgisayar: Taş")
            benimSkor += 1
        
        elif bilgisayarSecim == kagit:
            print("Sonuç: Berabere. Sen: Kağıt, Bilgisayar: Kağıt")
            
        elif bilgisayarSecim == makas:
            print("Sonuç: Bilgisayar Galip. Sen: Kağıt, Bilgisayar: Makas")
            bilgisayarSkor += 1
    
    #Makas seçtiğimiz durumlar
    if benimSecim == makas:

        if bilgisayarSecim == tas:
            print("Sonuç: Bilgisayar Galip. Sen: Makas, Bilgisayar: Taş")
            bilgisayarSkor += 1
            
        elif bilgisayarSecim == kagit:
            print("Sonuç: Galipsin. Sen: Makas, Bilgisayar: Kağıt")
            benimSkor += 1
            
        elif bilgisayarSecim == makas:
            print("Sonuç: Berabere. Sen = Makas, Bilgisayar: Makas")
    
    #Kazanma durumları
    if benimSkor == 3:
        print(f"Tebrikler kazandın! \nSen: {benimSkor}, Bilgisayar: {bilgisayarSkor}")
        
        devam = input("\nTekrar oynamak ister misin? (e/h): ") # e -> oyna h -> bitir

        if devam == "e":
            bilgisayarSkor = 0
            benimSkor = 0
            continue
        elif devam == "h":
            print("hoşçakal...")
            break

    elif bilgisayarSkor == 3:
        print(f"Maalesef kaybettin! \nSen: {benimSkor}, Bilgisayar: {bilgisayarSkor}")

        devam = input("\nTekrar oynamak ister misin? (e/h): ")

        if devam == "e":
            bilgisayarSkor = 0
            benimSkor = 0
            continue
        elif devam == "h":
            print("hoşçakal...")
            break
