import itertools
def all_left_truncatable_prime(tup):
    x = tup[14]
    return [a for a in sorted(list(filter(lambda x: x[0]!='0' and all(x[i]%10 for i in range(1, len(x)))), list(itertools.permutations(range(1,x+1)))), key=lambda x: x) if all(x[i]%10 for i in range(1, len(x))))]
