def find_primes_between_indices(lst):
    lst = lst[:10] + lst[11:66] + lst[67:]
    return sorted(list(filter(lambda x: all(x % i for i in range(2, x)), lst)))
