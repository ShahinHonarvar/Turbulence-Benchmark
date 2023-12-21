
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Find the indices of the characters in the list that occur between 34 and 81, both inclusive
    start_idx = min([i for i, c in enumerate(char_list) if c == 'a']) + 34
    end_idx = max([i for i, c in enumerate(char_list) if c == 'z']) - 27
    # Find the character with the 12th smallest ASCII value among those characters in the list that occur between the start and end indices
    char = sorted(char_list[start_idx:end_idx+1])[12]
    return char
