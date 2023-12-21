
def return_nth_smallest_ascii(string):
    # Create a dictionary to keep track of the ASCII values
    ascii_dict = {}

    # Iterate over the characters in the string
    for char in string:
        # If the character is not already in the dictionary, add it with an initial count of 1
        if char not in ascii_dict:
            ascii_dict[char] = 1

        # Otherwise, increment the count for the character
        else:
            ascii_dict[char] += 1

    # Sort the dictionary by value (i.e., the number of times each character appears)
    sorted_ascii_dict = sorted(ascii_dict.items(), key=lambda x: x[1], reverse=True)

    # Return the 18th smallest ASCII value among those characters in the string that occur between indices 33 to 60, both inclusive
    return sorted_ascii_dict[17][0]
