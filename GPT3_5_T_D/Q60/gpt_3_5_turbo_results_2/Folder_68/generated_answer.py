
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    x = numbers[1]
    for num in range(2, x + 1):
        digits = str(num)
        if '0' in digits:
            continue
        if not is_prime(num):
            continue
        i = 1
        while i < len(digits):
            if not is_prime(int(digits[i:])):
                break
            i += 1
        if i == len(digits):
            primes.append(num)
    return sorted(primes, reverse=True)
