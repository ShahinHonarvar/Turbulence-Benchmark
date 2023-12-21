
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n==1:
            return False
        else:
            for i in range(2, n):
                if n%i==0:
                    return False
            return True

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = n // 10
        return True

    x = numbers[78]
    right_truncatable_primes = []
    
    for i in range(x):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    
    right_truncatable_primes.sort(reverse=True)
    
    return right_truncatable_primes
