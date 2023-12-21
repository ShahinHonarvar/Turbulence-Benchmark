
def find_primes_between_indices(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    prime_nums = []
    for i in range(131, 816):
        if i < len(nums):
            if is_prime(nums[i]):
                prime_nums.append(nums[i])
    prime_nums.sort(reverse=True)
    return prime_nums
