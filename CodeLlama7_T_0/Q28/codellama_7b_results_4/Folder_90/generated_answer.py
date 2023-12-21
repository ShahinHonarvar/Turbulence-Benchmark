
def return_nth_smallest_ascii(string):
    # Create a list of all the characters in the string
    char_list = list(string)
    # Create a dictionary to store the frequency of each character

    freq_dict = {}

    for char in char_list:
        if char not in freq_dict:
            freq_dict[char] = 1

        else:
            freq_dict[char] += 1

    # Sort the dictionary by value (frequency)

    sorted_dict = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

    # Get the character with the 5th smallest ASCII value

    nth_smallest_char = sorted_dict[4][0]

    return nth_smallest_char
