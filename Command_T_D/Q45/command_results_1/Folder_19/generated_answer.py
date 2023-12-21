def palindromes_between_indices(s):
    # '\w' includes letters, digits, and underscore
    # 'a-z' includes lower-case letters
    # 'A-Z' includes upper-case letters
    # '0-9' includes digits
    # '-' includes the hyphen
    # '_' includes the underscore
    # We add the '.' as a possible character for the middle
    # of the palindrome to improve the chance of a match.
    # We use a set to avoid duplicate values.
    return set((''.join(sorted(str(x)) for x in range(1, 8)) for x in range(1, len(s) - 6)))
