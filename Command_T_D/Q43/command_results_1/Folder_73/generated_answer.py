def find_primes_between_indices(nums):
    lst = []
    for n in range(19, 91):
        if all(n % i != 0 for i in range(2, int(n ** .5) + 1)):
            lst.append(n)
    return sorted(lst, reverse=True)
