# Finds the sum of all primes below 2,000,000

import math

# Determines whether or not a number is prime
def is_prime(num):
    if num == 2 or num == 1:
        return True
    sqrt_num = math.ceil(math.sqrt(num)) + 1
    for i in range(2, sqrt_num):
        if num % i == 0:
            return False

    return True

def gen_primes(max_num):
    primes = []
    for num in range(2, max_num):
        if is_prime(num):
            primes.append(num)
    return sum(primes)

def main():
    print(gen_primes(2000000))

if __name__ == '__main__':
    main()
