def find_primes_between_indices(lst):
    res = []
    start = 11
    end = 41
    if len(lst) < start:
        return res
    if start <= len(lst) - end:
        for i in range(start, end):
            if lst[i] == 2 or lst[i] == 3:
                res.append(lst[i])
            elif lst[i] > 3:
                for j in range(2, int(lst[i**0.5]) + 1):
                    if lst[i] % j == 0:
                        break
                    elif lst[i] % j == 1:
                        res.append(lst[i])
                        break
    return res
