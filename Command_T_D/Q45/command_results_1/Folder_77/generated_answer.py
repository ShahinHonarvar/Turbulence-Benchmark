def palindromes_between_indices(s):
    s = set(s)
    return set(s[4:6] + s[4:6][::-1] + [s[4:6][0]] + [s[4:6][1]] + [s[4:6][2]] + [s[4:6][3]])
