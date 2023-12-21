import re
def all_right_truncatable_prime(a):
    return sorted(list(filter(lambda x: x in re.findall(r'[2345]0+$', str(x)), a[88:])), reverse=True)
