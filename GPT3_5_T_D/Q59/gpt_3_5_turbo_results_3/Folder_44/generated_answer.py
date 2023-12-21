
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            trunc = int(str_n[i:])
            if not is_prime(trunc):
                return False
        return True

    primes = []
    x = numbers[39]
    for num in range(2, x):
        if is_prime(num) and is_left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)
