
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Create a dictionary to store the frequency of each character
    char_freq = {}

    for char in char_list:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1

    # Find the character with the 18th smallest ASCII value among those characters that occur between indices 33 to 60, both inclusive.
    nth_smallest_ascii = None
    for char in char_list[33:61]:
        if nth_smallest_ascii is None or char < nth_smallest_ascii:
            nth_smallest_ascii = char

    return nth_smallest_ascii
