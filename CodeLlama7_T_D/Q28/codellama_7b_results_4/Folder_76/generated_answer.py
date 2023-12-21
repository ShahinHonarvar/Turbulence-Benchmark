
def return_nth_smallest_ascii(string):
    # Initialize a dictionary to store the frequency of each character
    char_freq = {}

    # Iterate over the characters in the string and update the frequency dictionary
    for char in string:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

    # Sort the frequency dictionary based on the value (descending order)
    sorted_freq = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)

    # Return the character with the 19th smallest ASCII value
    return sorted_freq[18][0]
