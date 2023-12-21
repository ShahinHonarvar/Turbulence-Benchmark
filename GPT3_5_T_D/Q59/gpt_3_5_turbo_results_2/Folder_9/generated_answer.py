
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[29]
    left_truncatable_primes = []
    for i in range(10, x):
        if is_prime(i):
            prime = str(i)
            is_left_truncatable = True
            for j in range(1, len(prime)):
                if not is_prime(int(prime[j:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                left_truncatable_primes.append(i)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes
