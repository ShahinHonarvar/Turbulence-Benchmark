def all_left_truncatable_prime(test_list):
    res = []
    for i in range(2, test_list[0]):
        prime = True
        str_num = str(i)
        while str_num:
            if str_num[0] == "0":
                break
            str_num = str_num[1:]
            if str_num in str(i):
                prime = False
                break
        if prime:
            res.append(i)
    return res
