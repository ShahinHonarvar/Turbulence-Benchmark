
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
        if x < 2:
            continue
        digits = str(x)
        if '0' in digits:
            continue
        left_truncatable = True
        right_truncatable = is_prime(x)
        for i in range(1, len(digits)):
            if not is_prime(int(digits[i:])):
                right_truncatable = False
                break
        for i in range(len(digits)-1, 0, -1):
            if not is_prime(int(digits[:i])):
                left_truncatable = False
                break
        if left_truncatable and right_truncatable:
            primes.append(x)
    primes.sort()
    return primes
