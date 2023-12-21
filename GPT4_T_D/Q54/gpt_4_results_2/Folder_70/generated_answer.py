
def all_right_truncatable_prime(nums):
    #check if an entered number is prime
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    
    #check if an entered number is  right-truncatable prime
    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = n // 10
        return True
    
    #return list of right_truncatable primes
    result = []
    x = nums[433]
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)
