def palindromes_of_specific_lengths(text):
    return set(text[22:95:].rfind("".join(str(i) for i in range(52, 55+1)), 1))
