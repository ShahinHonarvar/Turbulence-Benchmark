def all_left_truncatable_prime(tup):
    res = []
    for i in range(tup[0] + 1):
        j = str(i)
        while j and j[0] != "9":
            if int(j) == i:
                break
            j = int(j[1:])
        else:
            res.append(i)
    return sorted(res)
