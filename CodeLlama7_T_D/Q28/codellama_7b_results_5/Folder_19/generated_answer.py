
def return_nth_smallest_ascii(string):
    # Create a dictionary to store the frequency of each character
    char_freq = {}
    for char in string:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1
    # Sort the dictionary by value and then key
    sorted_dict = sorted(char_freq.items(), key=lambda x: (x[1], x[0])))
    # Return the character with the 13th smallest ASCII value
    return sorted_dict[12][0]
