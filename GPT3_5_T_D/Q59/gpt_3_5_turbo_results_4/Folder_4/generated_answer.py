
def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[96]
    primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        truncated_num = int(str(num)[1:])
        is_truncatable = True
        while truncated_num > 0:
            if not is_prime(truncated_num):
                is_truncatable = False
                break
            truncated_num = int(str(truncated_num)[1:])
        if is_truncatable:
            primes.append(num)
    return sorted(primes, reverse=True)
