def palindromes_of_specific_lengths(s):
    return set(s[i:i + 28].lower() for i in range(13, 99))
