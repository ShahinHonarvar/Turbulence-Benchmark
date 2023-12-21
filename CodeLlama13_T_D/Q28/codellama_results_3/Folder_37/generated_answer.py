
def return_nth_smallest_ascii(s):
    ascii_values = []
    for i in range(28, 67+1):
        if s[i] not in ascii_values:
            ascii_values.append(ord(s[i]))
    return chr(sorted(ascii_values)[14])
