def palindromes_of_specific_lengths(s):
    return {p for p in (s[i:j] for i in range(130, 295) for j in range(i, min(len(s) - 1, i + 158), -1)) if p[::-1] == p and p.lower() in 'qwertyuiopasdfghjklzxcvbnm'}
