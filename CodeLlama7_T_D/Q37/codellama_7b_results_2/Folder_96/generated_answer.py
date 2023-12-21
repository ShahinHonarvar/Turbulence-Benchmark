
def filter_chars(string):
    filtered_string = ""
    for char in string:
        if (char >= "!" and char <= "s") and (char >= string[86] and char <= string[92]):
            continue
        else:
            filtered_string += char

    return filtered_string
