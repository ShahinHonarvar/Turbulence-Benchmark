
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[33]
    primes = []

    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False

        while len(str(n)) > 2:
            if not is_prime(n):
                return False
            n = int(str(n)[1:-1])

        return is_prime(n)

    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            primes.append(i)

    return primes
