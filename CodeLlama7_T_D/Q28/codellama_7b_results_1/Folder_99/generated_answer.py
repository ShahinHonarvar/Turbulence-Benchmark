
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Create a dictionary to store the frequency of each character
    char_freq = {}

    # Iterate through the list of characters and calculate their frequency
    for char in char_list:
        if char not in char_freq:
            char_freq[char] = 1

        else:

            char_freq[char] += 1

    # Sort the dictionary by value (frequency)
    sorted_freq = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)

    # Get the character with the 8th smallest ASCII value
    nth_smallest = sorted_freq[7][0]

    return nth_smallest
