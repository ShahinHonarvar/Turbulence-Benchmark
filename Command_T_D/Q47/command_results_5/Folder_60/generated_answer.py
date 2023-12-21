def palindromes_of_specific_lengths(s):
    return set(x[23:-23] for x in s[24:-24] if x.lower() in x[23:-23] and len(x) in range(32, 35))
