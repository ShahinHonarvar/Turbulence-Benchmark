def palindromes_of_specific_lengths(str1):
    str1 = str1[11:93]
    if not str1:
        return set()
    return set(x[::-1] for x in str1[::2] if len(x) in (34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54))
