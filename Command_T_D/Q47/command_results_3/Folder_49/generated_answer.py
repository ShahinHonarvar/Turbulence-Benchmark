def palindromes_of_specific_lengths(text):
    return set(filter(lambda s: s[10:100] in text[10:100].lower() and len(s) in range(10, 50), map(str.rstrip, text[10:100])))
