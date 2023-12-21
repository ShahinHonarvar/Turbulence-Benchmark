def palindromes_of_specific_lengths(text):
    return set(text[11:-11].lower() for i in range(13, 67))
