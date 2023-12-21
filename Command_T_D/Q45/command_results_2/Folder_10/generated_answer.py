def palindromes_between_indices(s):
    s = set(s.lower())
    return set("".join(s[i:j] for i in range(len(s)) for j in range(i+1, min(len(s), i+6))))
