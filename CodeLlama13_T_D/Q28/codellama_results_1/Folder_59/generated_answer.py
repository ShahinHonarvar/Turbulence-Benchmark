
def return_nth_smallest_ascii(string):
    char_count = {}
    for i in range(0, 12):
        if string[i] in char_count:
            char_count[string[i]] += 1
        else:
            char_count[string[i]] = 1
    min_ascii_val = float('inf')
    for c, count in char_count.items():
        if count == 12 and ord(c) < min_ascii_val:
            min_ascii_val = ord(c)
    return chr(min_ascii_val)
