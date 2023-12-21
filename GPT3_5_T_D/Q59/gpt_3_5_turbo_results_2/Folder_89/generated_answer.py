
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[97]
    truncatable_primes = []
    for i in range(10, x):
        if is_prime(i):
            truncatable = True
            num = str(i)
            while truncatable and num != "":
                if not is_prime(int(num)):
                    truncatable = False
                num = num[1:]
            if truncatable:
                truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)
