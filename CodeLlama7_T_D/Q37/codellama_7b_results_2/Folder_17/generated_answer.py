
def filter_chars(string):
    filtered = ""
    for i, char in enumerate(string):
        if i >= 27 and i <= 29 and char >= ';' and char <= 'b':
            continue

        filtered += char

    return filtered
