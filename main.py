hello = "Hello Python"
print(hello)

name = "Kadir Birdal"
age = 28

getName = input("Adınız: ")
getFavoriteFood = input("En Sevdiğin Yemek: ")
message = getName + ", " + getFavoriteFood + " sever."
print(message)

# Basic Calculator
firstNumber = input("Birinci Sayı: ")
secondNumber = input("İkinci Sayı: ")
selectOperations = input("İşlem Seç - (+, -, *, /): ")

if selectOperations == "+":
    result = firstNumber + secondNumber
    print("Sonuç: " + result)
elif selectOperations == "-":
    result = firstNumber - secondNumber
    print("Sonuç: " + result)
elif selectOperations == "*":
    result = firstNumber * secondNumber
    print("Sonuç: " + result)
elif selectOperations == "/":
    result = firstNumber / secondNumber
    print("Sonuç: " + result)
else:
    print("Lütfen geçerli bir işlem seçin")