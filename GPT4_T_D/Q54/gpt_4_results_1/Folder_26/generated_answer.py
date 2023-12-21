
def all_right_truncatable_prime(nums):
    from sympy import isprime
    
    def truncate(num):
        while num:
            yield num
            num = num // 10
    
    def is_right_truncatable(num):
        return all(isprime(n) for n in truncate(num))

    x = nums[81]
    primes = []
    
    for num in range(x):
        if is_right_truncatable(num):
            primes.append(num)
            
    return sorted(primes, reverse=True)
