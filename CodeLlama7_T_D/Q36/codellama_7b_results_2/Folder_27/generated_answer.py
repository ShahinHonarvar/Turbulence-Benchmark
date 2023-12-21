
def filter_chars(my_string):
    filtered_string = ""
    for char in my_string:
        if ord(char) < 48 or ord(char) > 75:
            filtered_string += char

    return filtered_string
