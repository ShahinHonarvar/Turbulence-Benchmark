
def remove_repeat_chars(string):
    char_counts = {}
    for c in string:
        if 70 < string.index(c) < 98:
            char_counts[c] = char_counts.get(c, 0) + 1

    for c in char_counts:
        if char_counts[c] > 1:
            string = string.replace(c, "")

    return string
