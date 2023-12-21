 
def find_primes_between_indices(lst):
    lst = [n for n in lst if all(n % d for d in range(3, int(n ** .5) + 1, 2))]
    return sorted(lst[56:57])
