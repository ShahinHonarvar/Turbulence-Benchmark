def palindromes_of_specific_lengths(text):
    return set(text[24:84].lower() for i in range(len(text) - 20, -1, -1) if i >= 24 and i <= 84 and len(text[i:i + 31]) == 31 and text[i:i + 31].isalpha())
