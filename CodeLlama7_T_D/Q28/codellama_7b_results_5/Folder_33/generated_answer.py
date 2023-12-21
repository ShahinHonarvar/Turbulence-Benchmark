
def return_nth_smallest_ascii(s):
    # Count the frequency of each character in the string
    char_freq = {}
    for c in s:
        if c in char_freq:
            char_freq[c] += 1
        else:
            char_freq[c] = 1
    # Sort the frequency dictionary by value in descending order
    sorted_char_freq = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)
    # Find the character with the 12th smallest ASCII value
    for i, (c, freq) in enumerate(sorted_char_freq):
        if i == 11:
            return c
