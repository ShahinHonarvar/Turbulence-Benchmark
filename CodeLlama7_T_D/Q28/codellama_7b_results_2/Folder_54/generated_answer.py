
def return_nth_smallest_ascii(string):
    # Create a dictionary to store the counts of each character in the string
    char_counts = {}
    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    # Sort the dictionary by value (ascending) and get the indices of the characters
    sorted_indices = sorted(char_counts.items(), key=lambda x: x[1])
    # Get the character with the 17th smallest ASCII value among those characters in the string that occur between indices 12 to 87, both inclusive
    nth_smallest_ascii = sorted_indices[16][0]
    return nth_smallest_ascii
