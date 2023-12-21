
def return_nth_smallest_ascii(string):
    # Create a dictionary to store the frequency of each character in the string
    char_freq = {}
    for char in string:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1
    # Find the character with the 12th smallest ASCII value
    ascii_vals = []
    for char, freq in char_freq.items():
        ascii_vals.append((ord(char), freq)))
    ascii_vals.sort()
    nth_smallest_ascii = ascii_vals[12][0]
    return chr(nth_smallest_ascii)
