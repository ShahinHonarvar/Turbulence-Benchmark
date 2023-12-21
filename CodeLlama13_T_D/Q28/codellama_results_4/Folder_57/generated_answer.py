
def return_nth_smallest_ascii(string):
    chars = set()
    for i in range(17, 35):
        if string[i] in chars:
            continue
        chars.add(string[i])
    
    ascii_values = [ord(c) for c in sorted(chars)]
    return chr(ascii_values[18 - 1])
