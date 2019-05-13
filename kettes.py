import sys

def isPrime(n):


    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1 , 2):
        if n % i == 0:
            return False
    return True
try:
    bemenet = int(sys.argv[1])
    kimenet = open("ex11.txt", "w")
    for i in range(5000, 10001):
        temp = 0
        for j in range(2, bemenet):
            if i % j == 0:
                temp += 1
        if isPrime(bemenet) and temp == 0 and i % bemenet == 0:
            print(i ,file=kimenet)
    if not isPrime(bemenet):
        print("A bemenet nem primszam.")
    kimenet.close()
except ValueError :
 print("A bemenet nem egesz szam.")
except FileNotFoundError :
 print(" A megadott file nem talalhato.")
