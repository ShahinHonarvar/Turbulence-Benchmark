
def return_nth_smallest_ascii(chars):
    ascii_values = []
    
    for index in range(70):
        if index < len(chars):
            ascii_values.append(ord(chars[index]))
    
    sorted_ascii_values = sorted(ascii_values)
    
    return chr(sorted_ascii_values[9])
