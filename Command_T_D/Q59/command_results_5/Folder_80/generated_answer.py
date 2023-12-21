import re
def all_left_truncatable_prime(n):
    str_n = str(n[14])
    return sorted(list(filter(lambda x: x and str(x)[0] == str_n[0] and re.fullmatch(str_n[1:], str(x)), range(2, int(str_n) + 1))), reverse=True)
