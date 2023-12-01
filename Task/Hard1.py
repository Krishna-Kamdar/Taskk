def findprime(num, numm):
    prime = []
    for i in range(num, numm + 1):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count == 2:
            prime.append(i)

    return prime

num1 = int(input("Enter any number1: "))
num2 = int(input("Enter any number2: "))
print(findprime(num1, num2))