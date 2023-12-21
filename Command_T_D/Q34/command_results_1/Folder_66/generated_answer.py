def find_original_set(S):
    res = set(S)
    for i in range(len(S)):
        if len(S) == 1:
            break
        if S[i] <= res:
            continue
        else:
            res.update(S[i])
    return res
