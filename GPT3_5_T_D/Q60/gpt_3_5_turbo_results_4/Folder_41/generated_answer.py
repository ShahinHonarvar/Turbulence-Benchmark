
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
        if x < 10:
            continue
        if '0' in str(x):
            continue
        left_right_truncatable = True
        for i in range(len(str(x))):
            left = int(str(x)[i:])
            right = int(str(x)[:i + 1])
            if not is_prime(left) or not is_prime(right):
                left_right_truncatable = False
                break
        if left_right_truncatable:
            primes.append(x)
    return sorted(primes, reverse=True)
