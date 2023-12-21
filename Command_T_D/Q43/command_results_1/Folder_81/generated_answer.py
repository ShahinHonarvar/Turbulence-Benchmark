def find_primes_between_indices(lst):
    return sorted(lst[59:97]) if lst[59] <= 5**2*2**2 and lst[97] >= 3**3*5**2 else []
