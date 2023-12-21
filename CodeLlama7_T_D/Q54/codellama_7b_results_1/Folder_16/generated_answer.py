
def all_right_truncatable_prime(tuple):
    x = tuple[792]
    all_primes = []
    for i in range(x):
        if is_prime(i) and is_right_truncatable_prime(i):
            all_primes.append(i)
    return sorted(all_primes)

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

def is_right_truncatable_prime(n):
    digits = [int(digit) for digit in str(n)]
    for i in range(len(digits)):
        if not is_prime(int(''.join(map(str, digits[:i] + digits[i+1:])))))):
            return False

    return True
