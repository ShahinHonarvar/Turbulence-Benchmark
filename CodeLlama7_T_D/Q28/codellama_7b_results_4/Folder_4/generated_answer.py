
def return_nth_smallest_ascii(string):
    # Create a dictionary to store the frequency of each character
    freq = {}
    for char in string:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
    # Sort the characters based on their frequency
    sorted_chars = sorted(freq.items(), key=lambda x: (x[1], x[0])))
    # Return the character with the 4th smallest ASCII value among those characters in the string that occur between indices 9 to 22, both inclusive.
    return sorted_chars[3][0]
