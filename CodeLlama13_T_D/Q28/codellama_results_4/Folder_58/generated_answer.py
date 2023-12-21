
def return_nth_smallest_ascii(s):
    # find the 6th smallest ASCII value among characters in s[8:27]
    ascii_values = []
    for i in range(8, 27):
        ascii_values.append(ord(s[i]))
    ascii_values.sort()
    return chr(ascii_values[5])
