def checkValidation(num):
    if num <= 0:
        return False
    return True

def countDivision(num):
    divCount = 0
    for i in range(2, num):
        if num % i == 0:
            divCount += 1
    return divCount

def checkPrime(num):
    if countDivision(num) > 0 :
        return "not prime"
    return "prime"

if __name__ == "__main__":
    num = int(input("Enter you number:"))
    while checkValidation(num):
        isPrime = checkPrime(num)
        print(isPrime)
        num = int(input("Enter you number:"))
    print("END")
