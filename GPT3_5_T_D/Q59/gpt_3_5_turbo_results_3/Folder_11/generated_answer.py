
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[86]
    primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        truncatable = True
        while len(str(num)) > 1:
            if not is_prime(num):
                truncatable = False
                break
            num = int(str(num)[1:])
        if truncatable:
            primes.append(num)
    return sorted(primes)
