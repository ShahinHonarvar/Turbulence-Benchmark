
def all_left_right_truncatable_prime(numbers):
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_truncatable_prime(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
            if not is_prime(int(str_n[:i])):
                return False
        return True
    
    x = numbers[88]
    truncatable_primes = []
    for num in range(2, x+1):
        if is_prime(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
    
    return sorted(truncatable_primes)
