
def all_left_right_truncatable_prime(test_tup):
    res = []
    for j in range(max(test_tup) - 1):
        tmp = []
        for i in range(2, j + 1):
            if test_tup[i] <= 9:
                tmp.append(str(test_tup[i]))
            else:
                break
        for i in range(len(tmp)):
            if tmp[i] == '0':
                break
            elif tmp[i] == '1':
                res.append(test_tup[i])
            elif tmp[i] == '2':
                if test_tup[i] == test_tup[i - 1]:
                    res.append(test_tup[i])
                else:
                    break
            elif tmp[i] == '3':
                if test_tup[i] == test_tup[i - 1]:
                    res.append(test_tup[i])
                else:
                    break
            elif tmp[i] == '4':
                if test_tup[i] == test_tup[i - 1]:
                    res.append(test_tup[i])
                else:
                    break
            elif tmp[i] == '5':
                if test_tup[i] == test_tup[i - 1]:
                    res.append(test_tup[i])
                else:
                    break
            elif tmp[i] == '6':
                if test_tup[i] == test_tup[i - 1]:
                    res.append(test_tup[i])
                else:
                    break
            elif tmp[i] == '7':
                if test_tup[i] == test_tup[i - 1]:
                    res.append(test_tup[i])
                else:
                    break
            elif tmp[i] == '8':
                if test_tup[i] == test_tup[i - 1]:
                    res.append(test_tup[i])
                else:
                    break
            elif tmp[i] == '9':
                if test_tup[i] == test_tup[i - 1]:
                    res.append(test_tup[i])
                else:
                    break
        for i in range(len(res)):
            if res[i] == test_tup[i]:
                break
            else:
                res.append(test_tup[i])
    return res
