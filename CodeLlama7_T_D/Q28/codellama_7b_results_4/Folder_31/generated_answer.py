 def return_nth_smallest_ascii(string):
    # Initialize a dictionary to store the frequency of each character in the string
    char_freq = {}
    for char in string:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1
    # Sort the dictionary by value (frequency) in descending order
    sorted_freq = sorted(char_freq.items(), key=lambda x: (-x[1], x[0])))
    # Return the character with the 18th smallest ASCII value among those characters in the string that occur between indices 10 to 82, both inclusive.
    return chr((sorted_freq[17][0])[1]))
