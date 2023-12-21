
def return_nth_smallest_ascii(string):
    # Initialize a dictionary to store the frequency of each character in the string
    char_freq = {}

    # Iterate over the characters in the string and increment the frequency count for each character

    for char in string:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

    # Sort the dictionary by value (frequency) and return the key (character) at the specified index

    return sorted(char_freq.items(), key=lambda x: x[1], reverse=True)[14][0]
