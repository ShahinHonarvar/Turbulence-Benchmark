
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[86]
    primes = []
    for num in range(x-1, 1, -1):
        if '0' in str(num):
            continue
        truncatable = True
        for i in range(len(str(num))):
            trunc = int(str(num)[i:])
            if not is_prime(trunc):
                truncatable = False
                break
        if truncatable:
            primes.append(num)
    primes.sort(reverse=True)
    return primes
