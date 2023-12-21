def find_original_set(S):
    if len(S) == 1:
        return S[0]
    elif len(S) == 2:
        return {min(S), max(S)}
    else:
        return {x: min(S[x], S[x | y]) for x in S for y in S}
