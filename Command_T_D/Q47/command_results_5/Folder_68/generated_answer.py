def palindromes_of_specific_lengths(s):
    return set(p for i in range(50, 100) for p in s[i:i + i].lower() if p == p[::-1])
