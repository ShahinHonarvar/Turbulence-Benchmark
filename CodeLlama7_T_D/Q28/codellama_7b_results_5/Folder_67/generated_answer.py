
def return_nth_smallest_ascii(string):
    # Create a dictionary to store the frequency of each character
    char_freq = {}
    for char in string:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1
    # Get the list of characters that occur between indices 60 to 83, both inclusive
    char_list = []
    for i in range(60, 84):
        if string[i] not in char_list:
            char_list.append(string[i])
    # Sort the list of characters by their frequency

    sorted_char_list = sorted(char_list, key=lambda x: char_freq[x], reverse=True)
    # Return the 14th smallest ASCII value among the sorted list
    return sorted_char_list[13]
