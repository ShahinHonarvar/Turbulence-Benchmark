
def filter_chars(string):
    # Define a range of characters to filter
    chars_to_filter = range(ord('-'), ord('X') + 1)
    # Create a new string with filtered characters removed
    filtered_string = ''.join([char for char in string if char not in chars_to_filter])
    return filtered_string
