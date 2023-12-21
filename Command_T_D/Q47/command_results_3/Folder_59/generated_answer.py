def palindromes_of_specific_lengths(s):
    return {p for i in range(3, 16) for p in s[0:100].lower() if p == p[::-1]}
