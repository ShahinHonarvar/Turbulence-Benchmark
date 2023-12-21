def palindromes_of_specific_lengths(text):
    import re
    return set(re.findall(r'[a-z]{3,15}', text[0:100].lower()))
