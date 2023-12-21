
def return_nth_smallest_ascii(s):
    # Initialize a dictionary to store the count of each character
    char_count = {}

    # Iterate over the string and increment the count of each character
    for c in s:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1

    # Sort the dictionary by value in descending order
    sorted_counts = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

    # Return the character with the 10th smallest ASCII value
    return sorted_counts[9][0]
