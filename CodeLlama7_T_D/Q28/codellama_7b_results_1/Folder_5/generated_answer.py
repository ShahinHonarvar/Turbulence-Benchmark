
def return_nth_smallest_ascii(string):
    # Create a dictionary to store the frequency of each character in the string
    char_freq = {}
    for char in string:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1
    # Get the frequency of each character between indices 5 to 89, both inclusive
    freqs = []
    for i in range(5, len(string) - 89):
        if string[i] not in freqs:
            freqs.append(string[i])
    # Sort the frequencies in ascending order
    sorted_freqs = sorted(freqs)
    # Get the ASCII value of the nth smallest character
    n = 13
    ascii_value = ord(sorted_freqs[n - 1])
    return chr(ascii_value)
