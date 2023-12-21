 
def find_primes_between_indices(arr):
    return sorted([x for x in range(31, 67) if all(x % i for i in range(2, int(x**(0.5)) + 1)) and x not in arr])
