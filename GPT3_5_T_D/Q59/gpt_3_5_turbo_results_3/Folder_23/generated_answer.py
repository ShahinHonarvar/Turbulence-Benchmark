
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def all_truncatable_primes(n):
        truncatable_primes = []
        if is_prime(n):
            truncatable_primes.append(n)
            for i in range(1, len(str(n))):
                if is_prime(int(str(n)[i:])):
                    truncatable_primes.extend(all_truncatable_primes(int(str(n)[i:])))
        return truncatable_primes
    
    x = numbers[77]
    left_truncatable_primes = []
    for num in range(x-1, 0, -1):
        if '0' not in str(num):
            if all_truncatable_primes(num) == [num]:
                left_truncatable_primes.append(num)
    
    return left_truncatable_primes
