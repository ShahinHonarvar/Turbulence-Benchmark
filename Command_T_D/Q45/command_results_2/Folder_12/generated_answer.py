def palindromes_between_indices(s):
    return set(p for i in range(len(s) - 3, len(s) - 6) for p in (s[i:i + 4], s[i:i + 5], s[i:i + 6]) if p[::-1] == p)
