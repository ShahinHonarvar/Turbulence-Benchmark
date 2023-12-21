
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if is_prime(num) and '0' not in str(num):
            str_num = str(num)
            for i in range(1, len(str_num)):
                trunc_left = int(str_num[i:])
                trunc_right = int(str_num[:-i])
                if not is_prime(trunc_left) or not is_prime(trunc_right):
                    break
            else:
                primes.append(num)
    return sorted(primes)
