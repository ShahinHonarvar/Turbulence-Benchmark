
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(nums):
    primes = []
    for num in nums[157:736]:
        if is_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)
