#Problem7.py
#Project Euler problem 7

from NumberTests import isPrime

def main():
    number = 10001
    primeTotal = 0
    num = 1

    while primeTotal < number:
       num = num + 1
       if isPrime(num):
          primeTotal = primeTotal + 1

    print(num)

if __name__ == '__main__':
  main()
