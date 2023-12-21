 def return_nth_smallest_ascii(s):
    # Initialize a dictionary to store the frequency of each character in the string
    char_freq = {}
    # Iterate through the characters in the string and increment the frequency count for each character
    for char in s:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    # Sort the dictionary by key (character) and value (frequency count) in descending order
    sorted_dict = sorted(char_freq.items(), key=lambda x: (-x[1], x[0]))
    # Return the 15th smallest ASCII value among the characters that occur between indices 44 to 69, both inclusive
    return chr(sorted_dict[15][0])
