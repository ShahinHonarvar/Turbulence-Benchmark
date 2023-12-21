
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[992]
    truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            num = str(i)
            is_right_truncatable = True
            for j in range(1, len(num)):
                if not is_prime(int(num[:-j])):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                truncatable_primes.append(i)
    return sorted(truncatable_primes)
