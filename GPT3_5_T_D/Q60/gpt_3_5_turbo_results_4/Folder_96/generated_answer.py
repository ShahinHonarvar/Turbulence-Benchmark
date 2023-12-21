
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
        truncateable = True
        for i in range(len(str(x))):
            left_truncated = int(str(x)[i:])
            right_truncated = int(str(x)[:i+1])
            if left_truncated < 10 or right_truncated < 10:
                if not is_prime(left_truncated) or not is_prime(right_truncated):
                    truncateable = False
                    break
            else:
                if not is_prime(left_truncated) or not is_prime(right_truncated):
                    truncateable = False
                    break
        if truncateable:
            primes.append(x)
    return sorted(primes)
