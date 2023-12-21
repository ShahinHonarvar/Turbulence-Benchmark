import re
def all_right_truncatable_prime(tup):
    i = 43
    while i >= 3:
        if re.fullmatch(r'^[2-9][\d]{4}$', str(tup[i])):
            break
        i -= 1
    return sorted(list(range(2, i + 1)), key=lambda x: x)
