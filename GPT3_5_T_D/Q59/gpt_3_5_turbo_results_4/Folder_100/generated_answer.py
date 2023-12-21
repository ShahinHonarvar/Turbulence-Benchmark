
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[26]
    primes = []
    for n in range(2, x):
        if '0' not in str(n):
            truncatable = True
            num = str(n)
            while num:
                if not is_prime(int(num)):
                    truncatable = False
                    break
                num = num[1:]
            if truncatable:
                primes.append(n)
    return sorted(primes)
