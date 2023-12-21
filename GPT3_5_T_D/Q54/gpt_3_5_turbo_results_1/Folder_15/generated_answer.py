
def all_right_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    x = numbers[6]
    if x < 11:
        return []
    
    truncatable_primes = []
    for num in range(x-1, 10, -1):
        if all(is_prime(int(str(num)[:i])) for i in range(len(str(num)), 0, -1)):
            truncatable_primes.append(num)
    
    return sorted(truncatable_primes, reverse=True)
