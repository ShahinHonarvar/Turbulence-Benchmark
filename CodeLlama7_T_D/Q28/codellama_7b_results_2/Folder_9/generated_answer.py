
def return_nth_smallest_ascii(string):
    # Get the indices of the characters that occur between 10 and 90
    indices = [i for i, c in enumerate(string) if 10 <= i <= 90]
    # Sort the characters by their ASCII value
    sorted_chars = sorted([(ord(c), c) for c in string]), key=lambda x: x[0])
    # Return the character with the 20th smallest ASCII value
    return [char for ord, char in sorted_chars if ord == 20][0]
