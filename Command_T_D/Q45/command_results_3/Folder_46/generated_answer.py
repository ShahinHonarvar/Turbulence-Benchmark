def palindromes_between_indices(s):
    return {x[::-1] for x in ("".join(a) for a in (s[i:j] for i in range(4, 9) for j in range(4, 9)))}
