
def return_nth_smallest_ascii(string):
    # Find the indices of the characters in the string that occur between indices 15 and 21
    start_index = string.find(string[14]) + 1
    end_index = string.find(string[20]) - 1
    # Extract the substring containing the characters with the smallest ASCII values
    substrings = [string[i] for i in range(start_index, end_index + 1)]
    # Sort the characters by their ASCII values
    sorted_substrings = sorted(substrings, key=ord)
    # Return the character with the 6th smallest ASCII value
    return sorted_substrings[5]
