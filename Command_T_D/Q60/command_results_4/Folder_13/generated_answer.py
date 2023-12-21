
def all_left_right_truncatable_prime(test_list):
    res = []
    for n in test_list:
        if str(n).lstrip("0")[0] == "1" and str(n).rstrip("0")[-1] == "1":
            res.append(n)
    return res
