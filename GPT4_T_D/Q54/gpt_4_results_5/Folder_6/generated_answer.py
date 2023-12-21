
def all_right_truncatable_prime(t):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[:-i])):
                return False
        return True

    x = t[74]
    right_truncatable_primes = []
    for number in range(2, x):
        if is_right_truncatable(number):
            right_truncatable_primes.append(number)

    return sorted(right_truncatable_primes)
