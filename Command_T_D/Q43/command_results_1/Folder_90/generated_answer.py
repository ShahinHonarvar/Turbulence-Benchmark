def find_primes_between_indices(lst):
    # sort prime numbers from index 413 to index 448
    lst = lst[:413] + lst[413:448] + lst[448:]
    # filter prime numbers
    return sorted(set(lst) - set(lst[1:-1] + lst[2:-2] + lst[3:-3] + lst[4:-4]))
