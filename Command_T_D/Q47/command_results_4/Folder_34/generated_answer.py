def palindromes_of_specific_lengths(s):
    return set(x for x in s[200:300].lower() if x[0] in 'qwerty' and len(x) in range(10, 51))
