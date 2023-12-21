
def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if 163 <= ord(char) <= 658:
            if ord(char) > 40 and ord(char) < 91:
                continue

        filtered_string += char

    return filtered_string
