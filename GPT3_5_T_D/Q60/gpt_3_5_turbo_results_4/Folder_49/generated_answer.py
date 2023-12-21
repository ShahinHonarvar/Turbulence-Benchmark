
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if num < 10:
            continue
        num_str = str(num)
        if '0' in num_str:
            continue
        if not is_prime(num):
            continue
        left_truncatable = True
        right_truncatable = True
        for i in range(1, len(num_str)):
            left_num = int(num_str[i:])
            right_num = int(num_str[:-i])
            if not is_prime(left_num):
                left_truncatable = False
            if not is_prime(right_num):
                right_truncatable = False
        if left_truncatable and right_truncatable:
            primes.append(num)
    primes.sort()
    return primes
