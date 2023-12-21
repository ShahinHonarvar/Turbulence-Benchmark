
def return_nth_smallest_ascii(string):
    # Create a list of all the characters in the string that occur between indices 25 to 45, both inclusive
    char_list = []
    for i in range(25, 46):
        if string[i] not in char_list:
            char_list.append(string[i])
    # Sort the list of characters by their ASCII value

    sorted_list = sorted(char_list, key=lambda x: ord(x))
    # Return the character with the 11th smallest ASCII value

    return sorted_list[10]
