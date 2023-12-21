
def return_nth_smallest_ascii(string):
    # Get the indices of the characters between 35 and 52
    indices = [i for i, char in enumerate(string) if 35 <= char <= 52]
    # Sort the characters by their ASCII value
    sorted_characters = sorted(string[i] for i in indices))
    # Return the character with the 10th smallest ASCII value
    return sorted_characters[9]
