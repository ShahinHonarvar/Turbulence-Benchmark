
def remove_repeat_chars(string):
    # Create a dictionary to keep track of character frequencies
    char_freq = {}

    # Iterate over the string and update the frequency count for each character
    for char in string:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1

    # Remove all occurrences of characters that appear more than once between indices 37 and 43, both exclusive
    for i in range(37, len(string)):
        char = string[i]
        if char_freq[char] > 1:
            string = string.replace(char, "")

    # Return the altered string
    return string
