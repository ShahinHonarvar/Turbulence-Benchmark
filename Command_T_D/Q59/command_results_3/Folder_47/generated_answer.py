import re
def all_left_truncatable_prime(n):
    x = int(n[49])
    return sorted(list(set(re.findall(r"(([2-9]*)[2-9]\\1[234789]\\2[234789]\\3[234789]\\4[234789]\\5[234789]\\6[234789]\\7[234789]\\8[234789]\\9[234789]", re.I)))))
