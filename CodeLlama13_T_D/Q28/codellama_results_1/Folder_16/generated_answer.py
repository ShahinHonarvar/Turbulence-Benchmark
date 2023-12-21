
def return_nth_smallest_ascii(string):
    nth = 7
    indices = range(18, 46)
    ascii_values = []
    for i in indices:
        if string[i].isalpha():
            ascii_values.append(ord(string[i]))
    return chr(sorted(ascii_values)[nth-1])
