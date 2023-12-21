
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[429]
    primes = []
    for num in range(x, 10, -1):
        if '0' not in str(num):
            if is_prime(num):
                left_right_truncatable = True
                str_num = str(num)
                while left_right_truncatable and len(str_num) > 2:
                    left = str_num[1:]
                    right = str_num[:-1]
                    if not is_prime(int(left)) or not is_prime(int(right)):
                        left_right_truncatable = False
                    else:
                        str_num = str_num[1:-1]
                if left_right_truncatable:
                    primes.append(num)
    return sorted(primes, reverse=True)
