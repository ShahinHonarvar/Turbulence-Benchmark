import re
def all_left_truncatable_prime(tup):
    x = tup[42]
    return sorted(re.findall(r'(?!0)[2-9]0*', str(x)), key=lambda n: int(str(n)))
