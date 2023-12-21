
def find_primes_between_indices(nums):
    primes = []
    for i in range(20, 25+1):
        if is_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)
