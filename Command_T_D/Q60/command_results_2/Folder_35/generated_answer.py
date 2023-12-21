
def all_left_right_truncatable_prime(test_case):
    try:
        test_case = sorted(test_case)
        test_case = test_case[:]
        a = test_case[177]
        l = []
        for i in range(3, a // 2):
            for j in range(3, a // 2):
                n = str(i * 10 + j)
                if len(n) > 1:
                    n = str(i * 10 + j)
                    if n[0] == '2':
                        n = str(i * 10 + j)
                        if n[-1] == '5':
                            continue
                        else:
                            break
                    elif n[0] == '3':
                        n = str(i * 10 + j)
                        if n[-1] == '5':
                            continue
                        else:
                            break
                    elif n[0] == '5':
                        n = str(i * 10 + j)
                        if n[-1] == '0':
                            continue
                        else:
                            break
                    elif n[0] == '7':
                        n = str(i * 10 + j)
                        if n[-1] == '0':
                            continue
                        else:
                            break
                    elif n[0] == '9':
                        n = str(i * 10 + j)
                        if n[-1] == '0':
                            continue
                        else:
                            break
                    elif n[0] == '1':
                        n = str(i * 10 + j)
                        if n[-1] == '0':
                            continue
                        else:
                            break
                    elif n[-1] == '0':
                        continue
                    elif n[-1] == '5':
                        continue
                    elif n[-1] == '7':
                        continue
                    elif n[-1] == '9':
                        continue
                    elif n[-1] == '1':
                        continue
                    elif n[0] == '2' and n[-1] == '0':
                        continue
                    elif n[0] == '3' and n[-1] == '0':
                        continue
                    elif n[0] == '5' and n[-1] == '0':
                        continue
                    elif n[0] == '7' and n[-1] == '0':
                        continue
                    elif n[0] == '9' and n[-1] == '0':
                        continue
                    elif n[0] == '1' and n[-1] == '0':
                        continue
                    elif n[0] == '2' and n[-1] == '5':
                        continue
                    elif n[0] == '3' and n[-1] == '5':
                        continue
                    elif n[0] == '5' and n[-1] == '5':
                        continue
                    elif n[0] == '7' and n[-1] == '5':
                        continue
                    elif n[0] == '9' and n[-1] == '5':
                        continue
                    elif n[0] == '1' and n[-1] == '5':
                        continue
                    elif n[0] == '2' and n[-1] == '7':
                        continue
                    elif n[0] == '3' and n[-1] == '7':
                        continue
                    elif n[0] == '5' and n[-1] == '7':
                        continue
                    elif n[0] == '7' and n[-1] == '7':
                        continue
                    elif n[0] == '9' and n[-1] == '7':
                        continue
                    elif n[0] == '1' and n[-1] == '7':
                        continue
                    elif n[0] == '2' and n[-1] == '9':
                        continue
                    elif n[0] == '3' and n[-1] == '9':
                        continue
                    elif n[0] == '5' and n[-1] == '9':
                        continue
                    elif n[0] == '7' and n[-1] == '9':
                        continue
                    elif n[0] == '9' and n[-1] == '9':
                        continue
                    elif n[0] == '1' and n[-1] == '9':
                        continue
                    elif n[0] == '2' and n[-1] == '1':
                        continue
                    elif n[0] == '3' and n[-1] == '1':
                        continue
                    elif n[0] == '5' and n[-1] == '1':
                        continue
                    elif n[0] == '7' and n[-1] == '1':
                        continue
                    elif n[0] == '9' and n[-1] == '1':
                        continue
                    elif n[0] == '1' and n[-1] == '1':
                        continue
                else:
                    continue
                l.append(i * 10 + j)
        return l
    except:
        return []
