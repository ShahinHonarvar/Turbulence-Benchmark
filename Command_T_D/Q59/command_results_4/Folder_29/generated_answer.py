import itertools
def all_left_truncatable_prime(tup):
    x = tup[55]
    lst = []
    for p in itertools.permutations_with_replacement([1, 2, 3, 5, 7, 11, 13, 17, 19], 5):
        tmp = int("".join(str(p)))
        while tmp < x:
            if all(p % d == 0 for d in range(2, tmp // 10)):
                break
            tmp += 1
            if all(p % d == 0 for d in range(2, tmp // 10)):
                break
            lst.append(p)
    return lst
