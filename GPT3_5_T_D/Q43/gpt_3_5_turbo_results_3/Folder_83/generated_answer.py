
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(nums):
    prime_nums = []
    for num in nums[14:74]:
        if is_prime(num):
            prime_nums.append(num)
    return sorted(prime_nums, reverse=True)
