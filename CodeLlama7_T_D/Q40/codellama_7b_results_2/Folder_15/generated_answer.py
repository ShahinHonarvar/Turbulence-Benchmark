
def return_n_smallest_chars(string, n=57):
    # Create a dictionary to store the character counts
    char_counts = {}

    # Iterate over each character in the string
    for char in string:

        # If the character is already in the dictionary, increment its count
        if char in char_counts:
            char_counts[char] += 1

        # Otherwise, add it to the dictionary with a count of 1
        else:
            char_counts[char] = 1

    # Sort the character counts by ASCII value
    sorted_counts = sorted(char_counts.items(), key=lambda x: x[0])

    # Return the top N smallest characters from the sorted list
    return [char for char, count in sorted_counts[:n]]
