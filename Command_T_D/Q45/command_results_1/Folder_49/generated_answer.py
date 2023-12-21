def palindromes_between_indices(s):
    str_len = len(s)
    str_idx = 5
    str_idx_2 = 7
    lst_idx_5 = str_idx + str_idx_2
    lst_idx_6 = str_idx + str_idx_2 + 1
    lst_idx_7 = str_idx + str_idx_2 + 2
    res = set()
    for idx_5 in range(lst_idx_5, str_idx):
        for idx_6 in range(lst_idx_6, str_idx_2):
            for idx_7 in range(lst_idx_7, str_idx_2 + 1):
                idx_0 = idx_5
                idx_1 = idx_6
                idx_2 = idx_7
                idx_3 = str_idx_2 - 1
                idx_4 = str_idx - 1
                idx_0_lower = idx_0.lower()
                idx_1_lower = idx_1.lower()
                idx_2_lower = idx_2.lower()
                idx_3_lower = idx_3.lower()
                idx_4_lower = idx_4.lower()
                res.add(idx_0_lower + idx_1_lower + idx_2_lower + idx_3_lower + idx_4_lower)
    return res
