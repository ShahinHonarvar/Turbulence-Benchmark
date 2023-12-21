
def return_nth_smallest_ascii(string):
    # Create a dictionary to store the frequency of each character
    freq = {}
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    # Sort the dictionary by value
    sorted_freq = sorted(freq.items(), key=lambda x: x[1])
    # Return the character with the 13th smallest ASCII value
    return chr(sorted_freq[12][0]]))
