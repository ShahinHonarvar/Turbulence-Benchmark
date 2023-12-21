
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        n = str(n)
        if '0' in n:
            return False
        while n:
            if not is_prime(int(n)):
                return False
            n = n[1:]
        return True

    x = numbers[975]
    primes = []
    for num in range(2, x):
        if is_left_truncatable(num):
            primes.append(num)

    return sorted(primes, reverse=True)
