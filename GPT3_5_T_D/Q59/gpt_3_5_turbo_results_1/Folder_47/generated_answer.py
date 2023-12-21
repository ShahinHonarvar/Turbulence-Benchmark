
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[49]
    truncatable_primes = []
    for i in range(2, x):
        if '0' not in str(i):
            prime = True
            num = str(i)
            while len(num) > 1:
                num = num[1:]
                if not is_prime(int(num)):
                    prime = False
                    break
            if prime:
                truncatable_primes.append(i)
    return sorted(truncatable_primes)
