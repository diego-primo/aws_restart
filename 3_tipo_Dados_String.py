myString = "This is a string."
print('O valor da variável é "{}"'.format(myString))
print("O tipo da variável 'myValue' é: {} " .format(type(myString)))
print("O valor da variável é: {} e o tipo da classe é {}.\n" .format(str(myString),str(type(myString))))


firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print('A concatenação de "{}" e "{}" é "{}".\n' .format(str(firstString), str(secondString), str(thirdString)) )

name = input("Qual o seu nome? ")
print(name)
print("\n")

color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))