import itertools
def all_left_truncatable_prime(tup):
    res = list(itertools.chain.from_iterable(
    (l.split("0") for l in str(p).split(" prime") if l))
    for n in range(2, 55):
        l = str(tup[n])
        if l.split("0") and l.split(" prime"):
            res += [int(l[1:-3])]
    return sorted(res)
