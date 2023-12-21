
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[97]
    primes = []
    for num in range(2, x):
        num_str = str(num)
        if '0' in num_str:
            continue
        truncatable = True
        for i in range(1, len(num_str)):
            trunc_num_str = num_str[i:]
            if not is_prime(int(trunc_num_str)):
                truncatable = False
                break
        if truncatable and is_prime(num):
            primes.append(num)
    return sorted(primes)
