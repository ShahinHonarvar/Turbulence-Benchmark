def palindromes_between_indices(s):
    str_set = set(s[5:-5].lower())
    return set(s[5:-5] + s[6:-8] + s[7:-7] + s[8:-6] + s[9:-9])
