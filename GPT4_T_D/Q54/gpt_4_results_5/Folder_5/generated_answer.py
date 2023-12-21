
def all_right_truncatable_prime(arr):
    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    x = arr[55]
    truncatable_primes = []
    for i in range(2, x):
        if right_truncatable(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes)
