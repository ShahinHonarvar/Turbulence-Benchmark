
def return_nth_smallest_ascii(s):
    ascii_values = []
    for i in range(8):
        ascii_values.append(ord(s[i]))
    sorted_ascii_values = sorted(ascii_values)
    nth_smallest = sorted_ascii_values[7]
    return chr(nth_smallest)
