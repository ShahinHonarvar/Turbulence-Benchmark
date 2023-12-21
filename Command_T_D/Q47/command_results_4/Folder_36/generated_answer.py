def palindromes_of_specific_lengths(s):
    if not s:
        return set()
    if not (len(s) > 124 and len(s) < 283):
        return set()
    if not (len(s) > 115 and len(s) < 135):
        return set()
    return set(i[::-1] for i in s[124:-4:-2] if i[0].isalpha())
