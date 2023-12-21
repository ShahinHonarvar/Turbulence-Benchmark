
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[86]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            truncate = i
            while truncate > 10:
                truncate //= 10
                if not is_prime(truncate):
                    break
            else:
                primes.append(i)
    return sorted(primes)
