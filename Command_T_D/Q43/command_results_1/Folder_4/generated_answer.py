 
def find_primes_between_indices(nums):
    primes = []
    for i in range(24, 83):
        if all(num % d for d in range(2, int(num ** .5) + 1)):
            primes.append(i)
    return sorted(primes)
