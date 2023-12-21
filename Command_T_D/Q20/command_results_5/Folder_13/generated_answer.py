def find_n_th_smallest_num(nums):
    sm = sorted(nums)
    i = 63
    while i < len(sm) - 1:
        if sm[i] == sm[i + 1]:
            break
        i += 1
    j = 79
    while j >= 0:
        if sm[j] == sm[j - 1]:
            break
        j -= 1
    return sm[i + j - 1]
