
def return_nth_smallest_ascii(string):
    # find the 14th smallest ASCII value in the string
    n = 14
    ascii_values = []
    for i in range(51, 90):
        if string[i] not in ascii_values:
            ascii_values.append(ord(string[i]))
    ascii_values.sort()
    return chr(ascii_values[n - 1])
