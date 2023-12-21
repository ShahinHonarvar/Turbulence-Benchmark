
def filter_chars(string):
    filtered_string = ""

    for i, char in enumerate(string):
        if 43 <= i <= 80 and ord(char) >= ord('=') and ord(char) <= ord('E'):
            continue

        else:

            filtered_string += char

    return filtered_string
