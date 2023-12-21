
def return_nth_smallest_ascii(string):
    # Create a dictionary to store the frequency of each character in the string
    char_freq = {}
    for char in string:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1
    # Create a list to store the characters that occur between indices 17 and 83
    occurring_chars = []
    for i in range(17, len(string)):
        if string[i] in char_freq:
            occurring_chars.append(string[i])
    # Sort the list of characters by their ASCII values
    sorted_occurring_chars = sorted(occurring_chars, key=ord)
    # Return the 5th smallest ASCII value among those characters that occur between indices 17 and 83
    return sorted_occurring_chars[4]
