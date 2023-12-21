
def return_nth_smallest_ascii(string):
    # Create a dictionary to store the frequency of each character in the string
    freq = {}
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    # Sort the dictionary by value (frequency) in descending order
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    # Get the ASCII value of the character with the 20th smallest frequency
    ascii_value = sorted_freq[19][0]
    return chr(ascii_value)
