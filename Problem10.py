#Problem10.py
#Project Euler problem 10

from NumberTests import isPrime

def main():
    total = 0
    number = 2000000

    for num in range(2, number):
       if isPrime(num):
          total = total + num

    print(total)

if __name__ == '__main__':
  main()
