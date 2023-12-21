
def all_right_truncatable_prime(numbers):
    primes = []
    for x in numbers:
        for i in range(1, len(str(x)) + 1):
            if is_prime(int(str(x)[:-i])) and str(x)[-i] == '0':
                primes.append(int(str(x)[:-i]))
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
