
def return_nth_smallest_ascii(string):
    # Create a dictionary to store the frequency of each character in the string
    char_freq = {}
    for char in string:
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1
    # Sort the characters in the dictionary by their frequency
    sorted_chars = sorted(char_freq.items(), key=lambda x: (-x[1], x[0])))
    # Return the character with the 6th smallest ASCII value among those characters that occur between indices 9 to 59, both inclusive
    return sorted_chars[5][0]
