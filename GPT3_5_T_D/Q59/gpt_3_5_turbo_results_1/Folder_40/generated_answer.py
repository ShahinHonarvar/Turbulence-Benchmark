
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[10]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            prime = str(i)
            is_left_truncatable = True
            for j in range(1, len(prime)):
                if not is_prime(int(prime[j:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                primes.append(i)
    
    return sorted(primes, reverse=True)
