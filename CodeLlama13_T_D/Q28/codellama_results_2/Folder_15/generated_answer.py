
def return_nth_smallest_ascii(string):
    n = 6
    start = 0
    end = 5
    ascii_values = []
    for i in range(start, end + 1):
        ascii_values.append(ord(string[i]))
    ascii_values.sort()
    return chr(ascii_values[n - 1])
