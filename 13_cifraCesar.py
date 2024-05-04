#recebe um argumento de string (alphabet) e concatena, ou combina, a string fornecida consigo mesma
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

#recebe msg do usuário
def getMessage():
    stringToEncrypt = input("\nPlease enter a message to encrypt: ")
    return stringToEncrypt

#recebe msg chave criptografia do usuário    
def getCipherKey():
    shiftAmount = input( "\nPlease enter a key (whole number from 1-25): ")
    return shiftAmount

#Criptografando uma mensagem 
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            print(f'##>Antiga posição: {alphabet[position]}')
            encryptedMessage = encryptedMessage + alphabet[newPosition]
            print(f'####>Nova posição: {alphabet[newPosition]}')
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

#descriptografando uma mensage, usando o mesmo método de criptografia.
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

#função principal o qual chama as demais funcões
def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}\n')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}\n')
    
runCaesarCipherProgram()