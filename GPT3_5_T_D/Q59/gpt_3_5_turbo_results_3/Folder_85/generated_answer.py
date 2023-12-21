
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[94]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        truncatable = True
        while truncatable and num > 10:
            num = int(str(num)[1:])
            if not is_prime(num):
                truncatable = False
        if truncatable and is_prime(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)
