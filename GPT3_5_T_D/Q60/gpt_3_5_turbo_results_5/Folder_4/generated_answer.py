
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[96]
    truncatable_primes = []
    
    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        if not is_prime(n):
            return False
        if len(str(n)) <= 2:
            return True
        return is_truncatable_prime(int(str(n)[1:-1]))
    
    for num in range(x, 1, -1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    
    return sorted(truncatable_primes, reverse=True)
