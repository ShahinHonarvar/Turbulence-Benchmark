
def all_left_right_truncatable_prime(x):
    res = []
    for i in range(2, x + 1):
        str_i = str(i)
        if len(str_i) > 1:
            if str_i[0] != '0' and str_i[-1] != '0':
                if str_i[0] != '1' or str_i[-1] != '1':
                    str_i = str_i[1:-1]
                if len(str_i) > 1:
                    if str_i[0] != '0' and str_i[-1] != '0':
                        if str_i[0] != '1' or str_i[-1] != '1':
                            str_i = str_i[1:-1]
                            if len(str_i) == 2:
                                if str_i[0] == '2' and str_i[1] == '5':
                                    res.append(int(str_i))
                                if str_i[0] == '3' and str_i[1] == '5':
                                    res.append(int(str_i))
                                if str_i[0] == '5' and str_i[1] == '5':
                                    res.append(int(str_i))
                                if str_i[0] == '7' and str_i[1] == '5':
                                    res.append(int(str_i))
                                if str_i[0] == '3' and str_i[1] == '7':
                                    res.append(int(str_i))
                                if str_i[0] == '5' and str_i[1] == '7':
                                    res.append(int(str_i))
                                if str_i[0] == '7' and str_i[1] == '7':
                                    res.append(int(str_i))
                                if str_i[0] == '3' and str_i[1] == '3':
                                    res.append(int(str_i))
                                if str_i[0] == '5' and str_i[1] == '3':
                                    res.append(int(str_i))
                                if str_i[0] == '7' and str_i[1] == '3':
                                    res.append(int(str_i))
                                if str_i[0] == '3' and str_i[1] == '5':
                                    res.append(int(str_i))
                                if str_i[0] == '5' and str_i[1] == '5':
                                    res.append(int(str_i))
                                if str_i[0] == '7' and str_i[1] == '5':
                                    res.append(int(str_i))
                                if str_i[0] == '3' and str_i[1] == '7':
                                    res.append(int(str_i))
                                if str_i[0] == '5' and str_i[1] == '7':
                                    res.append(int(str_i))
                                if str_i[0] == '7' and str_i[1] == '7':
                                    res.append(int(str_i))
                                if str_i[0] == '3' and str_i[1] == '3':
                                    res.append(int(str_i))
                                if str_i[0] == '5' and str_i[1] == '3':
                                    res.append(int(str_i))
                                if str_i[0] == '7' and str_i[1] == '3':
                                    res.append(int(str_i))
                                if str_i[0] == '3' and str_i[1] == '5':
                                    res.append(int(str_i))
                                if str_i[0] == '5' and str_i[1] == '5':
                                    res.append(int(str_i))
                                if str_i[0] == '7' and str_i[1] == '5':
                                    res.append(int(str_i))
                                if str_i[0] == '3' and str_i[1] == '7':
                                    res.append(int(str_i))
                                if str_i[0] == '5' and str_i[1] == '7':
                                    res.append(int(str_i))
                                if str_i[0] == '7' and str_i[1] == '7':
                                    res.append(int(str_i))
                                if str_i[0] == '3' and str_i[1] == '3':
                                    res.append(int(str_i))
                                if str_i[0] == '5' and str_i[1] == '3':
                                    res.append(int(str_i))
                                if str_i[0] == '7' and str_i[1] == '3':
                                    res.append(int(str_i))
                                if str_i[0] == '3' and str_i[1] == '5':
                                    res.append(int(str_i))
                                if str_i[0] == '5' and str_i[1] == '
	