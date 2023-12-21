
def return_nth_smallest_ascii(string):
    # Create a dictionary to store the frequency of each character in the string
    char_freq = {}
    for char in string:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1
    # Sort the dictionary by value (frequency)
    sorted_dict = {k: v for k, v in sorted(char_freq.items(), key=lambda item: item[1], reverse=True)}
    # Get the character with the 7th smallest ASCII value
    nth_smallest_ascii = list(sorted_dict)[6]
    return nth_smallest_ascii
