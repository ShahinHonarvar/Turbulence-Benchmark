def palindromes_of_specific_lengths(text):
    return {p for p in text[11:-11].lower() if len(p) in range(37, 61)}
