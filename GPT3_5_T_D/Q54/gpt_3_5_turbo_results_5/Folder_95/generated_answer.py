
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[77]
    rt_primes = []
    for i in range(2, x):
        num = str(i)
        while num:
            if not is_prime(int(num)):
                break
            num = num[:-1]
        else:
            rt_primes.append(i)
    return rt_primes
