def all_right_truncatable_prime(n):
    #your code here
    lst = []
    for i in range(2, n[0]):
        d = str(i)
        while len(d) > 1:
            d = int(d[1:])
            if d == i:
                break
            elif d not in lst:
                lst.append(i)
    return lst
