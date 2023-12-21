
def return_nth_smallest_ascii(string):
    ascii_values = []
    for char in string[60:84]:
        if char not in ascii_values:
            ascii_values.append(ord(char))
    
    ascii_values.sort()
    return chr(ascii_values[13])
