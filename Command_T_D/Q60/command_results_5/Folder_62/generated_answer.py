
def all_left_right_truncatable_prime(x):
    res = []
    for i in range(2, x + 1):
        str_i = str(i)
        if len(str_i) == 1:
            continue
        elif str_i[0] == '0':
            continue
        elif str_i[0] == '1':
            if len(str_i) == 2:
                continue
            elif str_i[1] == '0':
                continue
            elif str_i[1] == '1':
                res.append(int(str_i))
        elif str_i[0] == '2':
            if len(str_i) == 2:
                continue
            elif str_i[1] == '0':
                continue
        elif str_i[0] == '3':
            if len(str_i) == 3:
                continue
            elif str_i[1] == '0':
                continue
            elif str_i[2] == '0':
                continue
            elif str_i[1] == '1':
                if str_i[2] == '0':
                    continue
                elif str_i[2] == '1':
                    res.append(int(str_i))
        elif str_i[0] == '4':
            if len(str_i) == 2:
                continue
            elif str_i[1] == '0':
                continue
        elif str_i[0] == '5':
            if len(str_i) == 3:
                continue
            elif str_i[1] == '0':
                continue
            elif str_i[2] == '0':
                continue
            elif str_i[1] == '1':
                if str_i[2] == '0':
                    continue
                elif str_i[2] == '1':
                    res.append(int(str_i))
        elif str_i[0] == '6':
            if len(str_i) == 3:
                continue
            elif str_i[1] == '0':
                continue
            elif str_i[2] == '0':
                continue
            elif str_i[1] == '1':
                if str_i[2] == '0':
                    continue
                elif str_i[2] == '1':
                    res.append(int(str_i))
        elif str_i[0] == '7':
            if len(str_i) == 3:
                continue
            elif str_i[1] == '0':
                continue
            elif str_i[2] == '0':
                continue
            elif str_i[1] == '1':
                if str_i[2] == '0':
                    continue
                elif str_i[2] == '1':
                    res.append(int(str_i))
        elif str_i[0] == '8':
            if len(str_i) == 3:
                continue
            elif str_i[1] == '0':
                continue
            elif str_i[2] == '0':
                continue
            elif str_i[1] == '1':
                if str_i[2] == '0':
                    continue
                elif str_i[2] == '1':
                    res.append(int(str_i))
        elif str_i[0] == '9':
            if len(str_i) == 3:
                continue
            elif str_i[1] == '0':
                continue
            elif str_i[2] == '0':
                continue
            elif str_i[1] == '1':
                if str_i[2] == '0':
                    continue
                elif str_i[2] == '1':
                    res.append(int(str_i))
        else:
            if len(str_i) == 2:
                continue
            elif str_i[1] == '0':
                continue
            elif str_i[1] == '1':
                if str_i[2] == '0':
                    continue
                elif str_i[2] == '1':
                    res.append(int(str_i))
    return res
