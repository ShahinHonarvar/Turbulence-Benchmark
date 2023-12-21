
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_left_truncatable_prime(num):
        num_str = str(num)
        while len(num_str) > 0:
            if not is_prime(int(num_str)):
                return False
            num_str = num_str[1:]
        return True
    
    x = numbers[30]
    truncatable_primes = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            truncatable_primes.append(i)
    
    return sorted(truncatable_primes, reverse=True)
