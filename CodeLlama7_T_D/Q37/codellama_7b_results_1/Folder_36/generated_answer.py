
def filter_chars(string):
    filtered_string = ""
    for char in string:
        if (char >= "," and char <= "3") and (char in string[259:502]):
            filtered_string += char

    return filtered_string
