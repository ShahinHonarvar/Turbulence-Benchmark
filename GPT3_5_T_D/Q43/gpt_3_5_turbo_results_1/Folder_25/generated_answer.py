
def find_primes_between_indices(nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    primes = [num for num in nums[52:54] if is_prime(num)]
    primes.sort()
    return primes
