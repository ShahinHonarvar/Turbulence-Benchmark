
def return_nth_smallest_ascii(string):
    ascii_values = []
    for i in range(19):
        if string[i] in ascii_values:
            continue
        ascii_values.append((ord(string[i]), string[i]))
    return sorted(ascii_values)[12][1]
