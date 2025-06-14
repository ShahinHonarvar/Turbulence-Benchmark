
def return_nth_smallest_ascii(string):
    # Initialize a dictionary to store the frequency of each character
    freq = {}

    # Iterate over the string and increment the frequency of each character
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # Sort the dictionary by value in descending order
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Return the character with the 6th smallest ASCII value
    return sorted_freq[5][0]
