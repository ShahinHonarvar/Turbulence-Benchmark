
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        
        while len(str_n) > 1:
            if not is_prime(int(str_n)):
                return False
            str_n = str_n[1:-1]
        
        # Check one-digit and two-digit primes
        return is_prime(int(str_n))
    
    result = []
    x = numbers[784]
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            result.append(num)
    
    return sorted(result)
