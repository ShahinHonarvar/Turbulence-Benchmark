
def return_nth_smallest_ascii(string):
    # Initialize a dictionary to store the frequency of each character in the string
    freq = {}

    for char in string:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1

    # Sort the dictionary by value (frequency) and then by key (character)
    sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0])))

    # Return the nth smallest ASCII value among the characters in the string
    return chr(sorted_freq[19][0])
