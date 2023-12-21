
def filter_chars(string):
    filtered = ""

    for i, char in enumerate(string):
        if (i >= 24 and i <= 79) and (char >= 'a' and char <= 'f'):
            continue

        filtered += char

    return filtered
