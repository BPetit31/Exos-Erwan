# Class.py
import random
    
class IEncryptionMethod():
    gap = 3
    def __init__(self):
        pass

    def encryptChar(self, plainchar):
        encryptionResult = ""
        for c in plainchar.lower():
            if c.isalpha(): c = (ord(c[0]) + self.gap-97) % 26 + 97; c = chr(c); encryptionResult += c
            elif c.isspace(): encryptionResult += c
            else: encryptionResult += c
        self.gap += 1
        print(f"Le message crypté est : {encryptionResult}")

    def decryptChar(self, cipherchar):
        decryptionResult = ""
        decryptionGap = self.gap - 1
        for c in cipherchar.lower():
            if c.isalpha(): c = (ord(c[0]) - decryptionGap-97) % 26 + 97; c = chr(c); decryptionResult += c
            elif c.isspace(): decryptionResult += c
            else: decryptionResult += c 
        print(f"Le message décrypté est : {decryptionResult}")

    def reset(self):
        self.gap = 3
        print("L'index est reset")

class OneTime(IEncryptionMethod):
    def __init__(self):
        self.alphabet = list(map(chr, range(97, 123)))
        self.key1 = random.choice(self.alphabet)
        self.key2 = random.choice(self.alphabet)
        self.keyList = []

    def vigenereEncryption(self, plainchar):
        i = 0
        vigenere = OneTime()
        vigenereEncryptionKey = vigenere.key1 + vigenere.key2
        if vigenereEncryptionKey in self.keyList: print("Clé déjà utilisée"); exit()
        encryptionResult = ""
        print(f"Clé : {vigenereEncryptionKey}")
        for c in plainchar.lower():
                if c.isalpha() == False: encryptionResult += c
                elif i % 2 == 0: c = (ord(c[0]) - 97 + ord(vigenere.key1[0]) - 97) % 26; encryptionResult += self.alphabet[c]; i += 1
                elif i % 2 == 1: c = (ord(c[0]) - 97 + ord(vigenere.key2[0]) - 97) % 26 ; encryptionResult += self.alphabet[c]; i += 1
        self.keyList.append(vigenere.key1 + vigenere.key2)
        print(encryptionResult)

    def vigenereReset(self):
        self.keyList = []; print("La liste est reset")