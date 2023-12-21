def palindromes_between_indices(s):
    return {p for p in palindromes(s) if p[:-1] in s[1:-1] and p[-1] in s[0:-1]}
def palindromes(s):
    for i in range(1, len(s)):
        if s[:i] == s[i:]:
            yield s[:i]
            yield s[i:-1]
            yield s[i:]
