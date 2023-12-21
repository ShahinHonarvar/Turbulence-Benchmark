
def return_nth_smallest_ascii(string):
    # Initialize a dictionary to store the frequency of each character in the string
    freq = {}
    for char in string:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
    # Sort the characters in the string based on their frequency
    sorted_chars = sorted(freq, key=lambda x: freq[x], reverse=True)
    # Return the character with the 13th smallest ASCII value among those characters in the string that occur between indices 1 to 46, both inclusive.
    return sorted_chars[12]
