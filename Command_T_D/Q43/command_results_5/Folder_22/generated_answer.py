 
def find_primes_between_indices(lst):
    lst = list(range(75, 85 + 1))
    lst = [str(x) for x in lst]
    primes = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] != lst[i + 1]:
                break
            if lst[i] * lst[j] == lst[i + 1]:
                primes.append(lst[i])
                break
    return sorted(primes)
