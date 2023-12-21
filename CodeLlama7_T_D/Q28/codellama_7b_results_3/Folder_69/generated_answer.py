
def return_nth_smallest_ascii(string):
    # Create a dictionary to store the frequency of each character in the string
    char_freq = {}
    for char in string:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1
    # Sort the dictionary by value (frequency) in descending order
    sorted_dict = dict(sorted(char_freq.items(), key=lambda x: x[1], reverse=True))
    # Return the character with the 7th smallest ASCII value
    return sorted_dict[7]
