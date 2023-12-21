import re
def all_right_truncatable_prime(n):
    return [x for x in range(2, n[0] + 1) if re.match(r'(2[89]7|3[0-9]7|5[0-8]7|6[5-8]7|7[2-9]7|8[2-9]7|9[2-9]7)', str(x))]
