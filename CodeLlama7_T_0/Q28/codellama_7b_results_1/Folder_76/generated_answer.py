
def return_nth_smallest_ascii(string):
    # Create a dictionary to store the frequency of each character in the string
    char_freq = {}
    for char in string:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1
    # Sort the dictionary by value (frequency) and get the character with the 19th smallest ASCII value
    sorted_dict = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)
    nth_smallest_ascii = sorted_dict[18][0]
    return nth_smallest_ascii
