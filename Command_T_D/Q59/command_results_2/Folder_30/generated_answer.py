def all_left_truncatable_prime(test_tup):
    res = []
    for num in range(test_tup[37]):
        if str(num).isdigit():
            tmp_str = str(num)
            while tmp_str:
                if all(str(x).isdigit() for x in range(10, int(tmp_str[0]))) and all(x == '0' or str(x).isdigit() for x in range(int(tmp_str[0]))) and all(str(x) == '0' or str(x).isdigit() for x in range(int(tmp_str[1]))):
                    res.append(num)
                    break
    return res
