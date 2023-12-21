
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[79]
    truncatable_primes = []
    for num in range(x, 10, -1):
        if is_prime(num):
            truncatable = True
            str_num = str(num)
            while truncatable and len(str_num) >= 2:
                str_num = str_num[1:-1]
                if not is_prime(int(str_num)):
                    truncatable = False
            if truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)
