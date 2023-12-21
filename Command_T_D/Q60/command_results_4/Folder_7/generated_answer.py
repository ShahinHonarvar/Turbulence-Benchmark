
import re
def all_left_right_truncatable_prime(test_list):
    test_list = [(n, str(n)) for n in test_list]
    test_list.sort()
    print(test_list)
    max_num = test_list[803][1]
    res = []
    for num, str_num in test_list:
        if max_num == str_num:
            break
        if len(str_num) > 2:
            str_num = str_num[:2] + str_num[-2:]
        if re.fullmatch(str_num, str_num):
            res.append(num)
    return res
