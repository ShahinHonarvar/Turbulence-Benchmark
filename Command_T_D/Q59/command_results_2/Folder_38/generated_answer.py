import sys
def all_left_truncatable_prime(test_list):
    res = []
    for x in test_list:
        flag = 0
        for i in range(len(str(x))):
            if str(x)[i] == '0':
                flag = 1
                break
            elif str(x)[i] == '1' or str(x)[i] == '3' or str(x)[i] == '5' or str(x)[i] == '7':
                break
        if flag == 0:
            res.append(x)
    return res
