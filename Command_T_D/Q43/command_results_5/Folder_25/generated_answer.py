def find_primes_between_indices(lst):
    primes = []
    for i in range(len(lst) - 1):
        if lst[i] <= 52 and lst[i + 1] <= 53:
            primes += find_primes(lst, i, i + 2)
            break
    return primes
def find_primes(lst, lst_idx, idx):
    res = []
    for i in range(lst_idx, idx):
        if lst[i] % 2 == 0 or lst[i] == 1:
            continue
        else:
            res += find_primes(lst, i, idx)
            break
    return res
