
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[43]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            num = str(i)
            truncatable = True
            while num != '':
                if not is_prime(int(num)):
                    truncatable = False
                    break
                num = num[:-1]
            if truncatable:
                primes.append(i)
    return sorted(primes)
