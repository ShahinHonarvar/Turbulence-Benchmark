
def all_left_right_truncatable_prime(numbers):
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        n = str(n)
        while len(n) > 1:
            if not is_prime(int(n)):
                return False
            n = n[1:-1]
        return True

    x = numbers[98]
    if x < 10:
        return primes

    for num in range(10, x+1):
        if is_prime(num) and is_truncatable_prime(num):
            primes.append(num)

    return primes
