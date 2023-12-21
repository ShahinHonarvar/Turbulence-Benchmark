import re
def all_right_truncatable_prime(test_list):
    return re.findall(r'(99+)[^0-9]*99', str(test_list[38]))
