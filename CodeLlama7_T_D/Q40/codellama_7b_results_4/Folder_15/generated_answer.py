
def return_n_smallest_chars(s):
    # Sort the characters of the input string in ascending order based on their ASCII values
    sorted_chars = sorted(s, key=lambda x: ord(x))
    # Return the first 57 characters of the sorted list
    return sorted_chars[:57]
