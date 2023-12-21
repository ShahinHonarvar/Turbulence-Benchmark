
def filter_chars(s):
    filtered = ""
    for i, c in enumerate(s):
        if i >= 299 and i < 418 and c > '9' and c < 'P':
            continue

        else:

            filtered += c

    return filtered
