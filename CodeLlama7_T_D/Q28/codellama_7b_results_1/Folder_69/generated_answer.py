
def return_nth_smallest_ascii(string):
    # Calculate the number of occurrences of each character in the string
    char_counts = {}
    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    # Find the character with the 7th smallest ASCII value among those characters in the string that occur between indices 67 to 77, both inclusive
    ascii_values = []
    for char, count in char_counts.items():
        if 67 <= string.index(char) <= 77:
            ascii_values.extend([ord(char)] * count))
    return chr(sorted(ascii_values)[6])
