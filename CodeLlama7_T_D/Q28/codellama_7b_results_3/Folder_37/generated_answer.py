
def return_nth_smallest_ascii(s):
    # Create a dictionary to keep track of the ASCII values and their frequencies
    ascii_dict = {}

    # Iterate over the characters in the string
    for c in s:

        # If the character is not already in the dictionary, add it with frequency 1
        if c not in ascii_dict:
            ascii_dict[c] = 1

        # Otherwise, increment the frequency of the character by 1
        else:
            ascii_dict[c] += 1

    # Sort the dictionary by ASCII value in ascending order
    sorted_ascii_dict = sorted(ascii_dict.items(), key=lambda x: x[0])

    # Return the character with the 15th smallest ASCII value
    return sorted_ascii_dict[14][0]
