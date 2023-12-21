
def return_nth_smallest_ascii(string):
    ascii_vals = []
    for i in range(0, 88):
        if string[i].isalpha():
            ascii_vals.append(ord(string[i]))
    ascii_vals.sort()
    return chr(ascii_vals[13])
