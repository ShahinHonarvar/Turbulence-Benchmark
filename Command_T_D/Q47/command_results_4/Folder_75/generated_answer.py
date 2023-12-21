def palindromes_of_specific_lengths(text):
    return set(pal for pal in text[30:75].lower() if len(pal) in range(23, 40))
