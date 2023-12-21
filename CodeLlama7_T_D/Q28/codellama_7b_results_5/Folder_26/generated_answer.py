
def return_nth_smallest_ascii(s):
    # Initialize a dictionary to store the frequency of each character
    freq = {}

    # Iterate through the string and update the frequency of each character
    for c in s:
        if c not in freq:
            freq[c] = 0
        freq[c] += 1

    # Sort the frequency dictionary by value in descending order
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Return the character with the 15th smallest ASCII value
    return sorted_freq[14][0]
