
def return_nth_smallest_ascii(string):
    chars = {}
    for i, c in enumerate(string):
        if i < 16:
            chars[c] = i
    sorted_chars = sorted(chars.items(), key=lambda x: x[1])
    return sorted_chars[15][0]
