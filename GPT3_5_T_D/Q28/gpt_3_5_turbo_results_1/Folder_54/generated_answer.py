
def return_nth_smallest_ascii(s):
    substring = s[12:88]
    ascii_values = [ord(char) for char in substring]
    sorted_values = sorted(ascii_values)
    return chr(sorted_values[16])
