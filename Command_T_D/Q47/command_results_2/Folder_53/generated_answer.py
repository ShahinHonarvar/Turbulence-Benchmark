def palindromes_of_specific_lengths(s):
    return {p for p in range(1, 300) if s[p-1:p+i] == s[p-1:p+i][::-1] for i in range(3, 10)}
