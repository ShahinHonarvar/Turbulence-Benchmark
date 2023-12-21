
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
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            left_trunc = int(str_n[i:])
            right_trunc = int(str_n[:i+1])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                return False
        return True
    
    x = numbers[6]
    truncatable_primes = []
    for i in range(2, x+1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)
