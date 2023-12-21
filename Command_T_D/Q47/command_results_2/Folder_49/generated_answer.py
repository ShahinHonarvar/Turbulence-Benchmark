def palindromes_of_specific_lengths(s):
    return set(p for i in range(10, 100) for j in range(10, 50) for p in s[i:j+1] if p == p[::-1])
