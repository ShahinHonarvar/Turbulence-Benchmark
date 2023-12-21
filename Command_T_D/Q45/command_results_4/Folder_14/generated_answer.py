def palindromes_between_indices(s):
    return set(pal for i in range(len(s)-3) for pal in (s[i:j+1] for j in range(i+4, min(i+5, len(s)))))
