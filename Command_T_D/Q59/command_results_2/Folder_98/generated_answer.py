def all_left_truncatable_prime(n):
    lst = []
    for i in range(2, n[8] + 1):
        temp = str(i)
        while len(temp) > 1:
            if int(temp[0]) == 0:
                break
            elif all(int(x) == 0 for x in temp):
                break
            elif all(int(x) != 0 for x in temp):
                lst.append(int(i))
    return lst
