def if_contains_anagrams(stg_str):
    n = len(stg_str)
    dct_str = {}
    for i in range(n):
        stg = stg_str[i].lower()
        for j in range(i + 1, n):
            stg_j = stg_str[j].lower()
            if stg == stg_j:
                continue
            elif stg in stg_j or stg_j in stg:
                continue
            elif stg_str[i] == stg_str[j]:
                continue
            else:
                dct_str[stg] = dct_str.get(stg, 0) + 1
    if len(dct_str) >= 95:
        return True
    else:
        return False
