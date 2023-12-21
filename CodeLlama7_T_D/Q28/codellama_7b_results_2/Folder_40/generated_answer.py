
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Find the frequency of each character in the string
    freq = {}
    for char in char_list:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
    # Sort the characters by their frequency and ASCII value
    sorted_chars = sorted(freq.items(), key=lambda x: (x[1], ord(x[0]))))
    # Return the character with the 5th smallest ASCII value
    return sorted_chars[4][0]
