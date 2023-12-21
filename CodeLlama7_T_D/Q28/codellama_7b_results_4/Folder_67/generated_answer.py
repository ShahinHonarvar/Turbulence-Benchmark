
def return_nth_smallest_ascii(string):
    # Get the indices of the characters in the string
    start = 60
    end = 83
    # Create a list of all the characters between the indices
    char_list = [char for char in string if start <= string.index(char) <= end]
    # Sort the list by ASCII value
    sorted_list = sorted(char_list, key=lambda x: ord(x))
    # Return the 14th smallest ASCII value
    return sorted_list[13]
