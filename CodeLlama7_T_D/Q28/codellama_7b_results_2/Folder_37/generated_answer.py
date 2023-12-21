
def return_nth_smallest_ascii(string):
    # Extract the characters between indices 28 and 67, both inclusive
    sub_string = string[28:67+1]
    # Initialize a dictionary to store the frequency of each character in the sub-string
    char_freq = {}

    # Count the frequency of each character in the sub-string

    for char in sub_string:
        if char not in char_freq:
            char_freq[char] = 1

        else:
            char_freq[char] += 1

    # Sort the dictionary by value in descending order

    sorted_dict = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)

    # Return the character with the 15th smallest ASCII value

    return sorted_dict[14][0]
