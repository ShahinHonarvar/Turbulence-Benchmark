
def all_left_right_truncatable_prime(limits):
    res = []
    for n in range(2, limits[0] + 1):
        for d in range(2, str(n).count("0") + 1):
            if str(n)[-1 - d] == "0":
                break
            elif str(n)[:d] == "0":
                break
            elif str(n)[-1 - d] != "0" and str(n)[:d] != "0":
                res += [n]
    return res
