import re
def all_left_truncatable_prime(n):
    l = []
    for i in range(2, int(n[30]) + 1):
        if is_left_truncatable_prime(str(i)):
            l.append(i)
    return l
def is_left_truncatable_prime(s):
    for c in s:
        if c == '0':
            return False
        if not re.match(r'^0*(10[0-9]*)$', s):
            return False
    return True
