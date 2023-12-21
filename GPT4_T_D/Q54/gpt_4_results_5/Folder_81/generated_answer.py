
def all_right_truncatable_prime(nums):
    def is_prime(n): 
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))

    def right_truncate(n):
        return [int(str(n)[:i]) for i in range(len(str(n)), 0, -1)]
    
    x = nums[98]    
    truncatable_primes = []
    for num in range(2, x):
        primes = right_truncate(num)
        if all(map(is_prime, primes)):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)
