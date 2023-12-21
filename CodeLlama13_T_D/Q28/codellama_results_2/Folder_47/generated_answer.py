
def return_nth_smallest_ascii(string):
    ascii_values = {}
    for i in range(3, 52+1):
        if string[i] not in ascii_values:
            ascii_values[string[i]] = ord(string[i])
    
    sorted_ascii_values = sorted(ascii_values.items(), key=lambda x: x[1])
    
    return sorted_ascii_values[7][0]
