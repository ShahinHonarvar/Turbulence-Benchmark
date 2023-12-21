
def return_nth_smallest_ascii(s):
    # Initialize a dictionary to store the frequency of each character
    freq = {}

    # Iterate through the string and update the frequency dictionary
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # Sort the frequency dictionary by value
    sorted_freq = sorted(freq.items(), key=lambda x: x[1])

    # Return the character with the 8th smallest ASCII value
    return sorted_freq[7][0]
