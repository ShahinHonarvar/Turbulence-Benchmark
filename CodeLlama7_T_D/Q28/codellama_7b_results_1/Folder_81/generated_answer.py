
def return_nth_smallest_ascii(string):
    # Create a dictionary to store the character frequencies
    freq = {}

    # Loop through each character in the string
    for char in string:

        # If the character is already in the dictionary, increment its frequency by 1
        if char in freq:
            freq[char] += 1

        # Otherwise, add it to the dictionary with a frequency of 1
        else:
            freq[char] = 1

    # Sort the dictionary by frequency in descending order
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Return the character with the 14th smallest ASCII value
    return sorted_freq[13][0]
