import itertools
def all_right_truncatable_prime(n):
    for i in range(2, n[100] + 1):
        if is_right_truncatable_prime(i):
            yield i
    for i in range(2, n[100] // 2 + 1):
        for j in range(2, int(str(i)[0] + '0') + 1):
            if is_right_truncatable_prime(10**(10**(i-1) + j-1)):
                yield 10**(10**(i-1) + j-1)
def is_right_truncatable_prime(n):
    # Check if n is a prime number
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Check all prime divisors of n
    for i in range(5, int(str(n)[0] + '0') + 1):
        if n % i == 0:
            return False
    return True
