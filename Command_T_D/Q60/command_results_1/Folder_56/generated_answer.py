
def all_left_right_truncatable_prime(test_list):
    res = []
    for i in test_list:
        while i >= 10:
            x = str(i)
            for j in range(len(x) - 1):
                if x[j] == '0':
                    break
            if x[len(x) - 1] == '0':
                break
            if len(x) > 1 and x[0] == '0':
                break
            if int(x[1:]) == int(x[0] + x[-1:]):
                res.append(i)
                break
    return res
