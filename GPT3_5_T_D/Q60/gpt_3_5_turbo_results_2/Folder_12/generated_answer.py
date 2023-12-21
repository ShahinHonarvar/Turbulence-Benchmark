
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    def truncatable_prime(n):
        if not is_prime(n):
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            left = int(str_n[i:])
            right = int(str_n[:len(str_n)-i])
            if not is_prime(left) or not is_prime(right):
                return False
        return True

    x = numbers[70]
    truncatable_primes = []
    for i in range(2, x+1):
        if truncatable_prime(i):
            truncatable_primes.append(i)

    return sorted(truncatable_primes, reverse=True)
