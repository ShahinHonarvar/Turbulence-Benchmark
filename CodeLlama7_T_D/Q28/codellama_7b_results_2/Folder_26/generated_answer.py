
def return_nth_smallest_ascii(string):
    # Initialize a dictionary to store the frequency of each character
    freq = {}

    # Iterate over the characters in the string and update the frequency dictionary
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # Sort the frequency dictionary by value (ascending)
    sorted_freq = sorted(freq.items(), key=lambda x: x[1])

    # Return the character with the 15th smallest ASCII value
    return chr(sorted_freq[14][0]])
