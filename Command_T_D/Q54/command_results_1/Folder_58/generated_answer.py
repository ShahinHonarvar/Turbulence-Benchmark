def all_right_truncatable_prime(n):
    lst = []
    for i in range(2, int(n[0]) + 1):
        j = str(i)
        if len(j) > 1 and j[0] == '2':
            continue
        elif len(j) == 1:
            lst.append(i)
        else:
            if j[0] == '5':
                lst.append(i)
            else:
                j = int(j[1:])
                if i * 10 <= n[1]:
                    lst.append(i)
                else:
                    if j == 2 or j == 5:
                        lst.append(i)
    return lst
