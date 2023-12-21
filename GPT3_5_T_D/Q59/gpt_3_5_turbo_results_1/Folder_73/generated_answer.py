
def all_left_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    x = numbers[97]
    for i in range(2, x):
        if '0' not in str(i) and all(is_prime(int(str(i)[j:])) for j in range(len(str(i)))): 
            primes.append(i)
    return primes
