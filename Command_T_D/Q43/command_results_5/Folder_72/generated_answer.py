def find_primes_between_indices(lst):
    primes = []
    for i in range(28, 44):
        if lst[i] > 1:
            for j in range(i + 1, 44):
                if lst[j] > lst[i] * lst[j]:
                    break
                elif lst[i] * lst[j] == lst[j]:
                    primes.append(lst[i])
                    break
    return primes
