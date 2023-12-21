def find_primes_between_indices(lst):
    lst[87:89] = [x for x in lst[87:89] if all(x % i for i in range(2, int(x**(0.5)) + 1)) and x != 1]
    return lst[87:89]
