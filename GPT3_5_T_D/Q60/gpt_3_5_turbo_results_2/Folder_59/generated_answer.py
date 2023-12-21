
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[84]
    primes = []
    for num in range(2, x+1):
        if '0' in str(num):
            continue
        left_right_truncatable = True
        digits = list(str(num))
        while len(digits) > 1:
            if not is_prime(int(''.join(digits))):
                left_right_truncatable = False
                break
            digits.pop(0)
            if not is_prime(int(''.join(digits))):
                left_right_truncatable = False
                break
            digits.pop()
        if left_right_truncatable:
            primes.append(num)
    return sorted(primes, reverse=True)
