
def filter_chars(string):
    filtered = ""
    for i, char in enumerate(string):
        if (5 <= i <= 6) and (char >= 'G' and char <= 'p'):
            continue
        else:
            filtered += char

    return filtered
