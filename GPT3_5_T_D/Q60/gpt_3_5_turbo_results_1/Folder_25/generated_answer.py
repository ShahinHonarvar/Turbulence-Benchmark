
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
        if is_prime(x) and '0' not in str(x):
            str_num = str(x)
            left_truncatable = True
            right_truncatable = True
            for i in range(1, len(str_num)):
                left_num = int(str_num[i:])
                right_num = int(str_num[:-i])
                if not is_prime(left_num) or not is_prime(right_num):
                    left_truncatable = False
                    right_truncatable = False
                    break
            if left_truncatable or right_truncatable:
                primes.append(x)
    return sorted(primes)
