
def return_nth_smallest_ascii(s):
    ascii_values = []
    for i in range(18, 67):
        if s[i].isalpha():
            ascii_values.append(ord(s[i]))
    ascii_values.sort()
    return chr(ascii_values[18])
