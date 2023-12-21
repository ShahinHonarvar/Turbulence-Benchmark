 def return_nth_smallest_ascii(string):
    # Create a dictionary to store the frequency of each character in the string
    char_freq = {}
    for char in string:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1
    # Sort the dictionary by value
    sorted_dict = dict(sorted(char_freq.items(), key=lambda item: item[1], reverse=True))
    # Get the frequency of the character at index 17
    freq_at_index_17 = char_freq[string[17]]
    # Get the frequency of the character at index 86
    freq_at_index_86 = char_freq[string[86]]
    # Calculate the difference in frequency between the characters at indices 17 and 86
    diff = abs(freq_at_index_17 - freq_at_index_86)
    # Return the character with the 15th smallest ASCII value among those characters that occur between indices 17 to 86, both inclusive.
    return sorted_dict[diff][15]
