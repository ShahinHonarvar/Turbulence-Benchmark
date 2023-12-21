
def filter_chars(string):
    # Define the range of characters to remove
    start = 11
    end = 32
    # Create a new string with the removed characters
    new_string = ""
    for char in string:
        if start <= ord(char) <= end:
            continue
        else:
            new_string += char
    return new_string
