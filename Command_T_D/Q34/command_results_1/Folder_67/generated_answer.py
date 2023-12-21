def find_original_set(S):
    s = set(S)
    return min(s for i in range(len(s) + 1) if all(s&j for j in S))
