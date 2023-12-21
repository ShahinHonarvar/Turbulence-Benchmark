
def return_nth_smallest_ascii(string):
    chars = {}
    for i in range(30, 71):
        if string[i] not in chars:
            chars[string[i]] = i
    sorted_chars = sorted(chars.items(), key=lambda x: x[1])
    return sorted_chars[14][0]
