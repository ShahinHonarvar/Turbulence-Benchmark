def palindromes_of_specific_lengths(s):
    return {p for i in range(103, 277) for j in range(i, 277) for p in s[i:j].split("") if p[::-1] == p}
