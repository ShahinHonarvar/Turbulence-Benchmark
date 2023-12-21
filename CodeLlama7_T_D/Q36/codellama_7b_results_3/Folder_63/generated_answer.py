
def filter_chars(string):
    filtered = ""
    for i, char in enumerate(string):
        if 26 < ord(char) < 80:
            continue

        else:

            filtered += char

    return filtered
