import re
def all_left_truncatable_prime(n):
    return [int(x) for x in re.findall(r'(2[1-9][0-9]*)[13579]', str(n[26])))]
