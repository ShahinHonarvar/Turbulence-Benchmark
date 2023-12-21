
def return_nth_smallest_ascii(string):
    ascii_values = []
    for char in string[9:23]:
        if char not in ascii_values:
            ascii_values.append(ord(char))
    return chr(sorted(ascii_values)[3])
