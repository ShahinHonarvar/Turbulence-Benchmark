
def all_right_truncatable_prime(numbers):
    x = numbers[97]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        while is_prime(n):
            n = int(str(n)[:-1])
            if n == 0:
                return True
        return False

    for num in range(2, x):
        if is_right_truncatable_prime(num):
            primes.append(num)

    return sorted(primes)
