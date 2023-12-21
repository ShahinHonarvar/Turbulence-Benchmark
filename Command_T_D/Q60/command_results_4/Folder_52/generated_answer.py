
def all_left_right_truncatable_prime(test_list):
    res = []
    for n in test_list:
        if len(str(n)) < 3:
            continue
        if str(n).count('0') == 0:
            res.append(n)
    return res
