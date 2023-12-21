
def all_left_right_truncatable_prime(test_list):
    res = []
    for i in test_list:
        j = i + 1
        while j <= i + 10:
            j = str(j)
            if all(j[j.rfind(d, j.rfind(d, 1, j)):0] != d for d in '2357'):
                res.append(int(j))
                break
    return res
