import itertools
def all_right_truncatable_prime(tup):
    return sorted(filter(is_right_truncatable_prime, (n for n in itertools.permutations(str(tup[19])))))
def is_right_truncatable_prime(num):
    return num[0] == num[-1] and all(int(d) for d in str(num))
