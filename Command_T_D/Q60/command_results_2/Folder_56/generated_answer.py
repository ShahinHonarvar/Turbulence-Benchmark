
import re

def all_left_right_truncatable_prime(test_list):
    list_left_right_truncatable_prime = []
    for t in test_list:
        s = str(t)
        while len(s) > 1:
            if re.match(r'^[13579][13579]0+$', s):
                list_left_right_truncatable_prime.append(t)
                break
            s = s[:-1]
    return list_left_right_truncatable_prime
