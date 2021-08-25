# Main.py 

from Class import *
caesar = IEncryptionMethod()
vigenere = OneTime()

def main():
    print(f"Index =  {caesar.gap}")
    askUser = input("Encoder = 1, décoder = 2, reset l'index = 3, chiffrement de Vigenere = 4, reset keyList = 5 ")
    if askUser == "1": messageToEncrypt = input("Message :"); caesar.encryptChar(messageToEncrypt)

    elif askUser == "2": messageToDecrypt = input("Message :"); caesar.decryptChar(messageToDecrypt)

    elif askUser == "3": caesar.reset()

    elif askUser == "4": codeToEncrypt = input("Message :"); vigenere.vigenereEncryption(codeToEncrypt)

    elif askUser == "5" : vigenere.vigenereReset()
        
    else: print("Ce choix n'est pas valable.")

main()    
while True:
    askUserContinue = input("Voulez-vous recommencer ? [o/n] ? ")
    if askUserContinue.lower() not in ('o', 'oui', 'n', 'non'): print("Mauvaise saisie"); continue
    if askUserContinue.lower() in ('o', 'oui'): main()
    else: 
        print("Adieu"); break   