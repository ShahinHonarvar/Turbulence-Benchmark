 
def find_primes_between_indices(nums):
    primes = [x for x in range(424, 552 + 1) if all(x % i for i in range(2, int(x ** .5) + 1)) and x not in nums]
    return sorted(primes, reverse=True)
