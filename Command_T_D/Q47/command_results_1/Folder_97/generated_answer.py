def palindromes_of_specific_lengths(s):
    return {p for p in s[28:-1] if p[::-1] in s[28:-1] and len(p) in range(38, 50)}
