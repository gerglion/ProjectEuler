import math

primes = [2]

# Determines whether or not a number is prime
def is_prime(num):
    global primes
    if num == 2 or num == 1:
        return True
    for i in primes:
        if math.sqrt(num) < i:
            break
        if num % i == 0:
            return False

    return True

def gen_primes(max_num):
    global primes
    for num in range(primes[0] + 1, max_num, 2):
        if is_prime(num):
            primes.append(num)
    return sum(primes)

def main():
    print(gen_primes(2000000))

if __name__ == '__main__':
    main()