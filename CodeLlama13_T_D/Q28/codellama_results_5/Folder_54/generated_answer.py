
def return_nth_smallest_ascii(string):
    ascii_values = []
    for char in string:
        if ord(char) >= 12 and ord(char) <= 87:
            ascii_values.append(ord(char))
    
    return chr(sorted(ascii_values)[16])
