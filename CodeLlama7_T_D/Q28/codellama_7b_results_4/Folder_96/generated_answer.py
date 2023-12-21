
def return_nth_smallest_ascii(string):
    # Initialize a dictionary to store the frequency of each character
    char_freq = {}

    # Iterate through the string and increment the frequency of each character
    for char in string:
        if char in char_freq:
            char_freq[char] += 1

        else:
            char_freq[char] = 1

    # Sort the dictionary by value (frequency)
    sorted_dict = dict(sorted(char_freq.items(), key=lambda x: x[1], reverse=True))

    # Return the character with the 18th smallest ASCII value
    return sorted_dict[list(sorted_dict)[17]]
