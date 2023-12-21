 
def find_primes_between_indices(lst):
    lst = [x for x in lst if all(x % i != 0 for i in range(2, x // 2 + 1))]
    return sorted(lst[13:69])
