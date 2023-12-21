import itertools
def all_left_truncatable_prime(test_list):
    res = list(map(str, sorted(list(filter(lambda x: x<25 and all(str(x).count(c)==1 for c in str(x)))), reverse=True)))
    return list(map(str, filter(lambda x: str(x) in res, itertools.permutations(str(test_list[25]), len(str(test_list[25]))))))
