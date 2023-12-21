
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(nums):
    primes = []
    start_index, end_index = 72, 72
    for i in range(start_index, end_index + 1):
        if is_prime(nums[i]):
            primes.append(nums[i])
    return sorted(primes)
