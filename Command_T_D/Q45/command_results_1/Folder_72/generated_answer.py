def palindromes_between_indices(s):
    return {p for i in range(len(s)-6, len(s)+1) for p in pal(s[i:i+7])}
def pal(s):
    r, l = s[::-1], s[:]
    return [r + l[i:i+6] for i in range(len(l)-5)]
