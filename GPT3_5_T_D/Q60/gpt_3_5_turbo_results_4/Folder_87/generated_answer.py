
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
        for i in range(2, len(str(x))):
            left_part = int(str(x)[:i])
            right_part = int(str(x)[-(i-1):])
            if left_part < 10 or right_part < 10:
                continue
            if not is_prime(left_part) or not is_prime(right_part):
                break
        else:
            primes.append(x)
    primes.sort(reverse=True)
    return primes
