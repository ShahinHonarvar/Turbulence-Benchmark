import re
def all_left_truncatable_prime(test_list):
    res = []
    for i in range(len(test_list)):
        res += re.findall(r'(2[1-9][0-9]*)', str(test_list[i] - 1))
    return res
