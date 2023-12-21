
def return_nth_smallest_ascii(s):
    # Find the 8th smallest ASCII value among the characters in the string
    ascii_values = []
    for char in s[17:65]:
        if char not in ascii_values:
            ascii_values.append(ord(char))
    ascii_values.sort()
    return chr(ascii_values[7])
