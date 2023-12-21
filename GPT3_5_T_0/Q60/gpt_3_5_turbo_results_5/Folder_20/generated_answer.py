
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
        if is_prime(x):
            x_str = str(x)
            if '0' in x_str:
                continue
            is_truncatable = True
            for i in range(1, len(x_str)):
                left_trunc = int(x_str[i:])
                right_trunc = int(x_str[:len(x_str)-i])
                if not is_prime(left_trunc) or not is_prime(right_trunc):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(x)
    return sorted(primes, reverse=True)
