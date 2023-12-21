import itertools
def all_left_truncatable_prime(n):
    # sort in descending order
    l = []
    for x in itertools.permutations(str(n[0])):
        # remove leading leftmost digit
        t = int(str(n[0])[1:]+x)
        # check if all resulting numbers are prime
        if all(x == '0' or x in str(p) for p in range(2, t+1) if p%2 == 0 or p%5 == 0):
            # add to list
            l.append(t)
    # return list
    return l
