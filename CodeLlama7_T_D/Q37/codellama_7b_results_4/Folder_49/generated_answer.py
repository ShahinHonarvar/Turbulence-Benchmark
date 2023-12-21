
def filter_chars(my_string):
    # Define the range of characters to check
    char_range = range(42, 97)
    # Create a new string with the filtered characters
    filtered_string = ""

    for char in my_string:
        if char in char_range and char >= "*" and char <= "b":
            continue
        else:
            filtered_string += char

    return filtered_string
