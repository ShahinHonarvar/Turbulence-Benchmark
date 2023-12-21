def all_right_truncatable_prime(test_tup):
    x = test_tup[39]
    res = []
    for y in range(2, x // 2):
        str_y = str(y)
        if str_y[-1] == "2" and str_y[0] == "2":
            continue
        elif str_y[-1] == "2":
            res.append(y)
            break
        elif str_y[-1] == "5":
            res.append(y)
            break
        elif str_y[-1] == "0":
            res.append(y)
            break
        elif str_y[-1] == "1":
            res.append(y)
            break
        elif str_y[-1] == "3":
            res.append(y)
            break
        elif str_y[-1] == "7":
            res.append(y)
            break
        elif str_y[-1] == "4":
            res.append(y)
            break
        elif str_y[-1] == "6":
            res.append(y)
            break
        elif str_y[-1] == "8":
            res.append(y)
            break
        elif str_y[-1] == "9":
            res.append(y)
            break
    return res
