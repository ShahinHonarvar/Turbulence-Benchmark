
def return_nth_smallest_ascii(string):
    # Create a dictionary to store the frequency of each character in the string
    char_freq = {}
    for char in string:
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1
    # Sort the dictionary by value and then by key
    sorted_freq = sorted(char_freq.items(), key=lambda x: (x[1], x[0])))
    # Return the character with the 13th smallest ASCII value
    return chr(sorted_freq[12][0])
