
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])):
                return False
        return True

    x = numbers[97]
    primes = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)
