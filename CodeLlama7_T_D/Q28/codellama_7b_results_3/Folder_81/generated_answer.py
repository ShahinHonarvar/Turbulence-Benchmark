
def return_nth_smallest_ascii(string):
    # Initialize a dictionary to store the frequency of each character in the string
    freq = {}

    # Iterate over each character in the string and increment its frequency count in the dictionary

    for char in string:

        if char in freq:

            freq[char] += 1

        else:

            freq[char] = 1


    # Sort the dictionary by key (character) and value (frequency count)

    sorted_freq = sorted(freq.items(), key=lambda x: (x[0], x[1])))

    # Return the character with the 14th smallest ASCII value among those characters in the string that occur between indices 0 to 13, both inclusive.

    return sorted_freq[13][0]
