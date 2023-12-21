
def return_nth_smallest_ascii(string):
    # Create a dictionary to store the frequency of each character
    char_freq = {}
    for char in string:
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1
    # Get the indices of the characters that occur between indices 47 to 70, both inclusive
    indices = [i for i, char in enumerate(string) if 47 <= i <= 70 and char in char_freq]
    # Sort the indices based on the frequency of each character
    sorted_indices = sorted(indices, key=lambda x: char_freq[string[x]]))
    # Return the character with the 14th smallest ASCII value among those characters in the string that occur between indices 47 to 70, both inclusive.
    return string[sorted_indices[13]]
