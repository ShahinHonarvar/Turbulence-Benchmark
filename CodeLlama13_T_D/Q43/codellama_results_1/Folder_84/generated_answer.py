
def find_primes_between_indices(nums):
    prime_nums = []
    for i in range(830, 849+1):
        if is_prime(nums[i]):
            prime_nums.append(nums[i])
    return sorted(prime_nums)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
