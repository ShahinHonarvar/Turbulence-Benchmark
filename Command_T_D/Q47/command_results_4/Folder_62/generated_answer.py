def palindromes_of_specific_lengths(text):
    return {i for i in range(26, 87) if i in text[::-1].lower() for j in range(52, 56)}
