
def return_nth_smallest_ascii(string):
    # Find the 14th smallest ASCII value among characters in string
    ascii_values = sorted([ord(c) for c in set(string)])[13]
    # Find the indices between which the character with this ASCII value occurs
    start, end = 28, 54
    while ord(string[start]) > ascii_values:
        start += 1
    while ord(string[end]) <= ascii_values:
        end -= 1
    # Return the character with this ASCII value in this range
    return string[start:end+1].count(chr(ascii_values))
