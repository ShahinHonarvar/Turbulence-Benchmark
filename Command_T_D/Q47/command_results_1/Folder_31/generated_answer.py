def palindromes_of_specific_lengths(text):
    return set(i[11:-11] for i in text[11:-83] if i.lower() == i[::-1].lower() and len(i) in range(37, 61))
