from random import choice

itemList = ["TAS", "KAGIT", "MAKAS"]
myScore = 0
pcScore = 0

def devamControl(secim: str):
    secim = secim.upper()
    if(secim == "E"): #devam
        return True
    elif secim == "H": #bitir
        return False

def secimControl(pcSecim, mySecim):
    global pcScore, myScore
    
    match pcSecim: 
        case "TAS":
            if mySecim == "TAS":
                print("\nBerabare!")
                
            elif mySecim == "KAGIT":                    
                myScore += 1
                print(f"\nKazandın! Sen: {myScore} PC: {pcScore}")
                
            else:
                pcScore += 1
                print(f"\nKaybettin! Sen: {myScore} PC: {pcScore}")
                
        case "KAGIT":
            if mySecim == "KAGIT":
                print("\nBerabare!")
                
            elif mySecim == "MAKAS":
                myScore += 1
                print(f"\nKazandın! Sen: {myScore} PC: {pcScore}")
                
            else:
                pcScore += 1
                print(f"\nKaybettin! Sen: {myScore} PC: {pcScore}")
                
        case "MAKAS":
            if mySecim == "MAKAS":
                print("\nBerabare!")
                
            elif mySecim == "TAS":
                myScore += 1
                print(f"\nKazandın! Sen: {myScore} PC: {pcScore}")
                
            else:
                pcScore += 1
                print(f"\nKaybettin! Sen: {myScore} PC: {pcScore}")
  
print("****OYUNDA BAŞARILAR****")
while True:
    pcSecim = choice(itemList)
    mySecim = input("\nTaş, kağıt, makas: ").upper()
    
    if mySecim == "TAŞ" or mySecim == "MAKAS" or mySecim == "KAĞIT":
        
        secimControl(pcSecim, mySecim)
        
        if(pcScore == 3):
            print(f"\nKaybettin! Bir dahaki sefere kazanırsın! Sen: {myScore} PC: {pcScore}")
            devam = input("\nTekrar oynayacak mısın?(E/H): ")
            secimSonuc = devamControl(devam)
            if secimSonuc:
                myScore = 0
                pcScore = 0
            else:
                print("\nOyun Bitti!")
                break
            
        elif(myScore == 3):
            print(f"\nKazandın, tebrikler! Sen: {myScore} PC: {pcScore}")
            devam = input("\nTekrar oynayacak mısın?(E/H): ")
            secimSonuc = devamControl(devam)
            if secimSonuc:
                myScore = 0
                pcScore = 0
            else:
                print("\nOyun Bitti!")
                break
    else:
        print("\nDüzgün yazınız!")
    