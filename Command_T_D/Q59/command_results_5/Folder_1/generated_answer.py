import re
def all_left_truncatable_prime(n):
    return [int(x) for x in re.findall(r'[2-9][^0]*', str(n[20])))]
