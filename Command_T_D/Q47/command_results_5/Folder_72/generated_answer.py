def palindromes_of_specific_lengths(str):
    return set(p for p in str[26:90].lower() if len(p) in range(27, 59))
