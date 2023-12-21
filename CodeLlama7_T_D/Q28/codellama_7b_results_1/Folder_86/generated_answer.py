
def return_nth_smallest_ascii(s):
    # Initialize a dictionary to store the character counts
    char_counts = {}

    # Iterate over the characters in the string
    for c in s:

        # If the character is already in the dictionary, increment its count
        if c in char_counts:
            char_counts[c] += 1

        # Otherwise, add the character to the dictionary with a count of 1
        else:
            char_counts[c] = 1

    # Sort the characters by their counts in descending order
    sorted_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)

    # Return the character with the 15th smallest ASCII value among those characters that occur between indices 44 to 69, both inclusive
    return sorted_chars[14][0]
