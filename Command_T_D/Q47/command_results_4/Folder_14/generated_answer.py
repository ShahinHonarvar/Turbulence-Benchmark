def palindromes_of_specific_lengths(s):
    return {p for i in range(10, 75) for j in range(i, i + 6) for p in (s[i:j], s[j:i]) if p == p[::-1] and p.lower() in 'abcdefghijklmnopqrstuvwxyz'}
