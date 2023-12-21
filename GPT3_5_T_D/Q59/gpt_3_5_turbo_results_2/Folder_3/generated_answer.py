
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[100]
    primes = []
    for i in range(1, x):
        num = str(i)
        if '0' in num:
            continue
        while num:
            if not is_prime(int(num)):
                break
            num = num[1:]
        else:
            primes.append(i)
    return primes
