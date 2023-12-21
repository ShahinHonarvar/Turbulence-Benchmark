import itertools
def all_left_truncatable_prime(lst):
    return sorted(list(filter(left_truncatable_prime, lst)))
def left_truncatable_prime(n):
    for i in range(1, len(str(n))):
        if str(n)[i-1] == '0':
            return False
        elif not all(str(n)[:i] in '2357' for n in range(1, int(str(n)[:i])+1)):
            return False
    return True
