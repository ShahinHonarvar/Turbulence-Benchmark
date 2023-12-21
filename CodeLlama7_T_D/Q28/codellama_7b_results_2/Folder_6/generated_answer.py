
def return_nth_smallest_ascii(s):
    # Create a dictionary to store the character counts
    char_counts = {}

    # Iterate over the string and increment the count of each character
    for c in s:
        if c in char_counts:
            char_counts[c] += 1
        else:
            char_counts[c] = 1

    # Sort the dictionary by value (decreasing order)
    sorted_char_counts = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)

    # Find the character with the 11th smallest ASCII value
    nth_smallest_ascii = None
    for i, (c, count) in enumerate(sorted_char_counts):
        if count == 11:
            nth_smallest_ascii = c
            break

    return nth_smallest_ascii
