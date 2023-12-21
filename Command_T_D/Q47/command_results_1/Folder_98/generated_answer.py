def palindromes_of_specific_lengths(s):
    return set(p for p in range(5, 80 + 1) if p == len(p) and p <= 20 and s[i:i + p].lower() == s[i:i + p][::-1].lower() for i in range(len(s) - p))
