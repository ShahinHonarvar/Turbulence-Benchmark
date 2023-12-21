
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[177]
    primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        truncatable = True
        n = num
        while n > 0:
            if not is_prime(n):
                truncatable = False
                break
            n = int(str(n)[1:])
        if truncatable:
            primes.append(num)
    return sorted(primes)
