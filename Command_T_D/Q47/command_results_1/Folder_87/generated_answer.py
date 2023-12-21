def palindromes_of_specific_lengths(s):
    return set(x[11:-11] for x in s[11:-11] if len(x) in (34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54) and x.lower() in x)
