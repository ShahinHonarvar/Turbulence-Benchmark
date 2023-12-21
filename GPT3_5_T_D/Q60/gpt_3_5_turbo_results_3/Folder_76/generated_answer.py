
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
        digits = str(x)
        if '0' in digits:
            continue
        left_truncatable = True
        right_truncatable = True
        for i in range(len(digits)-1):
            left_part = int(digits[i+1:])
            right_part = int(digits[:len(digits)-i-1])
            if not is_prime(left_part) or not is_prime(right_part):
                left_truncatable = False
                right_truncatable = False
                break
        if left_truncatable or right_truncatable:
            primes.append(x)
    primes.sort(reverse=True)
    return primes
