
def return_nth_smallest_ascii(string):
    chars = set(string[12:56])
    ascii_values = []
    for char in chars:
        ascii_values.append(ord(char))
    
    ascii_values.sort()
    return chr(ascii_values[16])
