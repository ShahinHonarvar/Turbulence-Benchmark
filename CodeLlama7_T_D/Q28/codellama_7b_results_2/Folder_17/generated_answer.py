
def return_nth_smallest_ascii(string):
    # Create a dictionary to store the frequency of each character in the string
    char_freq = {}
    for char in string:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    # Sort the dictionary by value in descending order
    sorted_dict = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)
    # Return the character with the 4th smallest ASCII value among those characters in the string that occur between indices 4 to 33, both inclusive.
    return sorted_dict[3][0]
