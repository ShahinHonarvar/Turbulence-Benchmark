def all_left_truncatable_prime(num_tup):
    x = num_tup[7]
    res = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            res.append(num)
    return res
def is_left_truncatable_prime(num):
    str_num = str(num)
    while str_num:
        if str_num[0] == '0':
            return False
        str_num = str_num[1:]
        if str_num in '2357':
            return False
    return True
