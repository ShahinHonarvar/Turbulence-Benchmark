def palindromes_of_specific_lengths(s):
    return set(x for x in s.lower() if 65 <= x.rfind('a') <= 99 and len(x) in range(26, 34))
