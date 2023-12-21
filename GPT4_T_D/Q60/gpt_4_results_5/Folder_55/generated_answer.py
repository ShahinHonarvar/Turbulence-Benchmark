
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        for i in range(len(str(n)), 0, -1):
            if not is_prime(int(str(n)[:i])):
                return False
        return True

    x = numbers[73]
    truncatable_primes = []
    
    for n in range(11, x+1, 2):
        if '0' in str(n):
            continue
        if is_truncatable(n):
            truncatable_primes.append(n)
    
    return sorted(truncatable_primes, reverse=True)
