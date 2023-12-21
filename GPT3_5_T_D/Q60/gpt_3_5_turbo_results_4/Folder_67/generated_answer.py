
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def all_left_right_truncatable_prime(numbers):
    primes = []
    for number in numbers:
        if is_prime(number):
            digits = str(number)
            is_truncatable = True
            for i in range(1, len(digits)):
                left_truncated = int(digits[i:])
                right_truncated = int(digits[:i])
                if not is_prime(left_truncated) or not is_prime(right_truncated):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(number)
    return sorted(primes, reverse=True)
