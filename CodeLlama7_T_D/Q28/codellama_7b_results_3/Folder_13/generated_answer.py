
def return_nth_smallest_ascii(string):
    # Find the indices of the characters in the string
    indices = [i for i, char in enumerate(string) if char != ""]
    # Filter the indices to get the ones between 47 and 80
    filtered_indices = [index for index in indices if 47 <= index <= 80]
    # Get the characters corresponding to the filtered indices
    characters = [string[i] for i in filtered_indices]
    # Sort the characters by their ASCII values
    sorted_characters = sorted(characters, key=ord)
    # Return the character with the 4th smallest ASCII value
    return sorted_characters[3]
