
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for x in numbers:
        if x < 10:
            continue
        if is_prime(x) and '0' not in str(x):
            left_truncatable = True
            right_truncatable = True
            for i in range(1, len(str(x))):
                left_num = int(str(x)[i:])
                right_num = int(str(x)[:-i])
                if not is_prime(left_num):
                    left_truncatable = False
                    break
                if not is_prime(right_num):
                    right_truncatable = False
                    break
            if left_truncatable and right_truncatable:
                primes.append(x)
    return sorted(primes)
