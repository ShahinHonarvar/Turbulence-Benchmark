
def return_nth_smallest_ascii(s):
    # find the 5th smallest ASCII value among those characters in the string that occur between indices 29 to 33, both inclusive
    ascii_values = []
    for i in range(29, 34):
        if s[i] not in ascii_values:
            ascii_values.append(ord(s[i]))
    ascii_values.sort()
    return chr(ascii_values[4])
