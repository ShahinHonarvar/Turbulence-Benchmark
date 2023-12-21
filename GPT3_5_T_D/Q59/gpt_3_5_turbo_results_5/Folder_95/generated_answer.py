
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
        while len(str_n) > 1:
            str_n = str_n[1:]
            if not is_prime(int(str_n)):
                return False
        return True

    x = numbers[77]
    primes = []
    for num in range(2, x):
        if is_prime(num) and '0' not in str(num) and is_left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)
