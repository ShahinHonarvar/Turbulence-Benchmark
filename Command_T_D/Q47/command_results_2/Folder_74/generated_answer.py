def palindromes_of_specific_lengths(s):
    if not s:
        return set()
    i = 30
    j = 84
    return set(s[i:j+1].lower() for i in range(i, j+1) if s[i:j+1] == s[i][::-1])
