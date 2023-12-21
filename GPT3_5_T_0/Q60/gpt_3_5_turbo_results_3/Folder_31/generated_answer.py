
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
        if x < 23:
            continue
        x_str = str(x)
        if '0' in x_str:
            continue
        if not is_prime(x):
            continue
        left_truncatable = True
        right_truncatable = True
        for i in range(1, len(x_str)):
            left_num = int(x_str[i:])
            right_num = int(x_str[:-i])
            if not is_prime(left_num):
                left_truncatable = False
            if not is_prime(right_num):
                right_truncatable = False
            if not left_truncatable and not right_truncatable:
                break
        if left_truncatable or right_truncatable:
            primes.append(x)
    return sorted(primes, reverse=True)
