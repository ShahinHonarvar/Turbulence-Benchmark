def palindromes_of_specific_lengths(s):
    return set(map(str.lower, s[100:300:2] if len(s) >= 100 else s[100:300]))
