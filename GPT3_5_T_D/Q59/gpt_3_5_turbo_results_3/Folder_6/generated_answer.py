
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[74]
    primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        truncatable = True
        for i in range(len(str(num))):
            truncated_num = int(str(num)[i:])
            if not is_prime(truncated_num):
                truncatable = False
                break
        if truncatable:
            primes.append(num)
    return sorted(primes)
