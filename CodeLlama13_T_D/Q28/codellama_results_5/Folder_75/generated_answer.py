
def return_nth_smallest_ascii(string):
    nth = 9
    characters = set(string[62:83])
    ascii_values = sorted([ord(c) for c in characters])
    return chr(ascii_values[nth-1])
