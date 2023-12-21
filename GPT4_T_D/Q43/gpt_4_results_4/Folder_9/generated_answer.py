
def find_primes_between_indices(nums):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2,num):
            if (num % i) == 0:
                return False
        return True

    prime_nums = [num for num in nums[16:72] if is_prime(num)]
    return sorted(prime_nums)        
