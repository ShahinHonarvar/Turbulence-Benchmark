
def return_nth_smallest_ascii(s):
    # Find the 16th smallest ASCII value among the characters in s[5:83]
    ascii_values = []
    for c in s[5:83]:
        if c not in ascii_values:
            ascii_values.append(ord(c))
    ascii_values.sort()
    return chr(ascii_values[15])
