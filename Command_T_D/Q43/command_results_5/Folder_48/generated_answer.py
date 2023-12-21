def find_primes_between_indices(lst):
    lst = sorted(set(lst) - set(range( 261, 459+1, 2)) )
    return [i for i in lst if all(i % j != 0 for j in range(3, int(i**(0.5))+1, 2))]
