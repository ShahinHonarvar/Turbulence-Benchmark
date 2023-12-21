
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[0]
    right_truncatable_primes = []
    
    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        n = str(n)
        while n:
            if not is_prime(int(n)):
                return False
            n = n[:len(n)-1]
        return True
    
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    
    return sorted(right_truncatable_primes, reverse=True)
