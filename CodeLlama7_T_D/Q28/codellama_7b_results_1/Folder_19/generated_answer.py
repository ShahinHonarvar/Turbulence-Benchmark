
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Initialize a dictionary to keep track of the ASCII values and their counts
    ascii_dict = {}
    # Iterate through the characters in the string
    for char in char_list:
        # If the character is not already in the dictionary, add it with a count of 1
        if char not in ascii_dict:
            ascii_dict[char] = 1
        # Otherwise, increment the count by 1
        else:
            ascii_dict[char] += 1
    # Sort the dictionary by value (i.e., the count of each character) in descending order
    sorted_ascii_dict = sorted(ascii_dict.items(), key=lambda x: x[1], reverse=True)
    # Get the 13th element in the sorted dictionary (the ASCII value with the 13th smallest count among all characters in the string)
    ascii_value = sorted_ascii_dict[12][0]
    return ascii_value
