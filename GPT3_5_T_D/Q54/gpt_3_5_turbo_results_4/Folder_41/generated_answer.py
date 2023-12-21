
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def all_right_truncatable_prime(numbers):
    primes = []
    x = numbers[46]
    for i in range(x-1, 0, -1):
        num = str(i)
        truncatable = True
        while len(num) > 0:
            if not is_prime(int(num)):
                truncatable = False
                break
            num = num[:-1]
        if truncatable:
            primes.append(i)
    return sorted(primes, reverse=True)
