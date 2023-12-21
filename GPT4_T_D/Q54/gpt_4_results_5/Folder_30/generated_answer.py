
def all_right_truncatable_prime(numbers):
    x = numbers[37]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sqrt_n = int(n**0.5) + 1
        for i in range(3, sqrt_n, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        str_n = str(n)
        return all(is_prime(int(str_n[i:])) for i in range(len(str_n)))

    for n in range(2, x):
        if is_prime(n) and is_truncatable(n):
            primes.append(n)

    return sorted(primes, reverse=True)
