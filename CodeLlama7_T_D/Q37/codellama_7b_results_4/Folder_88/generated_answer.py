 def filter_chars(string):
    filtered = ""
    for i, char in enumerate(string):
        if (char >= '@' and char <= 'p') and (i >= 69 and i <= 80):
            continue

        filtered += char

    return filtered
