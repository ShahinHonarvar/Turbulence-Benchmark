
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
            str_x = str(x)
            if '0' in str_x:
                continue
            is_truncatable = True
            for i in range(1, len(str_x)):
                left_trunc = int(str_x[i:])
                right_trunc = int(str_x[:i])
                if not is_prime(left_trunc) or not is_prime(right_trunc):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(x)
    return sorted(primes)
