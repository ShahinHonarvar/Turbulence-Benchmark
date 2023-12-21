def palindromes_of_specific_lengths(s):
    return set(p for p in s[12:92].lower() if p[0] in 'a' and p[-1] in 'z' and len(p) in range(17, 66))
