#problem 3
'''
n = input("enter a number: ")
digits = sorted(n)
print("the minimal number you can form with n's digits is: ", ''.join(digits))
'''

#problem 7
'''
def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = input("enter a number: ")
while True:
    p = int(n) + 1
    q = int(n) + 3
    if isPrime(p) and isPrime(q):
        print("the next twin primes after " + n + " are: " + str(p) + " and " + str(q))
        exit()
'''

#problem 15
'''
def sumDiv(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum

n = input("enter a number: ")
x = int(n) - 1
while x > 0:
    if str(x) == str(sumDiv(x)):
        print(str(x) + " is a perfect number")
        exit()
    else:
        x -= 1
print("there is no perfect number smaller than " + str(n))
'''