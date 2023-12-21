
def return_nth_smallest_ascii(s):
    n = 5
    low, high = 17, 83
    ascii_values = []
    for i in range(low, high + 1):
        if s[i] not in ascii_values:
            ascii_values.append(ord(s[i]))
    return chr(sorted(ascii_values)[n - 1])
