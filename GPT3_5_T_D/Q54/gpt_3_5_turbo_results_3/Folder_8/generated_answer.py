
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
        
    right_truncatable_primes = []
    x = numbers[41]
    
    def check_prime(n):
        if is_prime(n):
            if n < x:
                right_truncatable_primes.append(n)
                for i in range(10):
                    check_prime(n * 10 + i)
                
    for i in range(2,10):
      check_prime(i)
      
    return sorted(right_truncatable_primes, reverse=True)
