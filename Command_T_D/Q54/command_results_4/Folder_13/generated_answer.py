import re
def all_right_truncatable_prime(test_list):
    list = []
    for i in test_list:
        str_i = str(i)
        str_i = re.sub(r'\d+$', '', str_i)
        if str_i:
            list.append(int(str_i))
    return list
