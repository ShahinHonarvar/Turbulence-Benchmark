def palindromes_between_indices(s):
    return {p for i in range(len(s) - 6) for p in map(str.lower, ("".join(s[i:j+8]), s[i:j+8])) if p[::-1] == p}
