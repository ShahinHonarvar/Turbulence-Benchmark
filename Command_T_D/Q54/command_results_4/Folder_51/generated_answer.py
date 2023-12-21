import re
def all_right_truncatable_prime(a):
    x = a[54]
    return sorted(filter(lambda n: re.fullmatch(r'^[2-9]99$', str(n)), range(2, x // 2)))
