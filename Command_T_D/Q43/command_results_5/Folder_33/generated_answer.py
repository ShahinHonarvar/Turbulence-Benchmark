def find_primes_between_indices(nums):
    lst = []
    for i in range(289, 381):
        if all(n % k != 0 for k in range(2, i // 2)):
            lst.append(i)
    return sorted(lst, reverse=True)
