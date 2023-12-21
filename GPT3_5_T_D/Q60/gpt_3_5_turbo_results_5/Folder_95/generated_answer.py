
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for x in numbers:
        if x < 11:
            continue
        str_x = str(x)
        if '0' in str_x:
            continue
        left = int(str_x[:-1])
        right = int(str_x[1:])
        if is_prime(left) and is_prime(right):
            primes.append(x)
    primes.sort()
    return primes
