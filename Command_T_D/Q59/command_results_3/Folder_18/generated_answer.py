def all_left_truncatable_prime(lim):
    lst = []
    i = 1
    while i < lim[0]:
        j = 1
        while j < lim[0] - i:
            if str(i * 10 ** (j - 1))[0] in "2357":
                break
            j += 1
        else:
            lst.append(i)
            break
        i *= 10 ** (j - 1)
    return lst
