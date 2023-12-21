
def return_nth_smallest_ascii(string):
    # Get the list of unique characters in the string
    unique_chars = set(string)
    # Initialize a dictionary to store the frequency of each character
    char_freq = {}
    for char in unique_chars:
        # Calculate the frequency of each character
        char_freq[char] = string.count(char)
    # Sort the characters by their frequency
    sorted_chars = sorted(char_freq, key=lambda x: char_freq[x])
    # Return the 17th smallest ASCII value among the sorted characters
    return chr(ord(sorted_chars[16]) + 1)
