
def filter_chars(string):
    filtered = ""
    for i in range(114, 639 + 1):
        char = string[i]
        if char >= '!' and char <= 'x':
            continue

        filtered += char

    return filtered
