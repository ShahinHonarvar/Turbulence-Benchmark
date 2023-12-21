
def return_n_smallest_chars(string):
    # Create a list of all distinct characters in the string
    chars = sorted(set(string))

    # Sort the list in ascending order based on ASCII value
    chars.sort()

    # Return the first 58 characters of the sorted list
    return chars[:58]
