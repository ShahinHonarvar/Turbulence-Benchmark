
def return_nth_smallest_ascii(string):
    # Create a dictionary to store the frequency of each character in the string
    char_freq = {}
    for char in string:
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1
    # Find the index of the 18th smallest ASCII value
    ascii_values = []
    for char, freq in char_freq.items():
        ascii_values += [ord(char)] * freq
    ascii_values.sort()
    nth_smallest_ascii = ascii_values[17]
    return chr(nth_smallest_ascii)
