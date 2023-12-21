
def all_left_right_truncatable_prime(lims):
    l = []
    for i in range(3, lims[0] + 1, 2):
        if str(i) in ("0", "1", "2"):
            continue
        for j in range(i + 1, lims[0] + 1, 2):
            if str(j) in ("0", "1", "2"):
                continue
            k = str(i) + str(j)
            if k[0] == "0" or k[-1] == "0":
                continue
            if int(k) == int(k[0] + k[1:]) == int(k[-1] + k[:-1]):
                l.append(int(k))
    return l
