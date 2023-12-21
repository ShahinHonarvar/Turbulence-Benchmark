
def all_left_right_truncatable_prime(test_list):
    res = []
    test_list = [int(i) for i in str(min(test_list))][:3]
    test_list = [test_list[-1]]
    for j in range(2, len(test_list)):
        if test_list[j] == '0':
            break
        test_list.append(test_list[j])
    test_list.sort()
    test_list.reverse()
    for i in range(len(test_list)):
        if test_list[i] == '0':
            break
        if test_list[i] == '1':
            res.append(test_list[i])
            continue
        test_list[i] = '0'
        test_list[i + 1] = '1'
        res.append(test_list[i])
        test_list[i] = '1'
        test_list[i + 1] = '0'
        res.append(test_list[i])
    return res
