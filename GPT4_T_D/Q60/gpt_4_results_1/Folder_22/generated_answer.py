
from itertools import permutations

def is_prime(n):
    if n in (0, 1):
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(T):
    x = T[85]

    digits = '123456789'
    truncatable_primes = []

    for l in range(1, len(str(x))+1):
        for perm in permutations(digits, l):
            number = int(''.join(perm))
            if number > x:
                break
            if '0' not in str(number):
                length = len(str(number))
                is_truncatable_prime = True
                for i in range(length):
                    if (not is_prime(int(str(number)[i:]))) or (not is_prime(int(str(number)[:length-i]))):
                        is_truncatable_prime = False
                        break
                if is_truncatable_prime:
                    truncatable_primes.append(number)

    return sorted(truncatable_primes)
