def palindromes_of_specific_lengths(s):
    return set(p for p in s[10:-10:-1] if p[0] in 'qwertyuiopasdfghjklzxcvbnm' and len(p) in range(24, 53))
