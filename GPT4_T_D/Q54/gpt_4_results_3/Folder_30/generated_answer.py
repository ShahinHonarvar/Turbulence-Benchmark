
def all_right_truncatable_prime(numbers):
    x = numbers[37]
    
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                return False
        return True

    def is_right_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable(i):
            right_truncatable_primes.append(i)
            
    return sorted(right_truncatable_primes, reverse=True)
