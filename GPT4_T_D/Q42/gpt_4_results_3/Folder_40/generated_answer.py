
def prime_factors(numbers):
    def is_prime(num):
        if num <= 1:
            return False
        elif num <= 3:
            return True
        elif num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def get_factors(num):
        primes = set()
        for i in range(1, num + 1):
            if num % i == 0 and is_prime(i):
                primes.add(i)
        return primes

    return get_factors(numbers[7])
