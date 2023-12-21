
def return_nth_smallest_ascii(string):
    # Create a dictionary to store the frequency of each character in the string
    char_freq = {}
    for char in string:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1
    # Sort the dictionary by value (frequency) and get the top 10 characters
    sorted_dict = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)[:10]
    # Get the ASCII value of the 10th character in the list
    ascii_value = ord(sorted_dict[9][0])
    return chr(ascii_value)
