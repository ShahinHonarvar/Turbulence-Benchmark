import itertools
def all_left_truncatable_prime(n):
    n = list(n)
    x = n[70]
    #your code here
    return sorted(set(itertools.filter(lambda x: x.lstrip("0").is_prime(), x)
