
def return_nth_smallest_ascii(string):
    chars = {}
    for i in range(5):
        if string[i] in chars:
            continue
        else:
            chars[string[i]] = ord(string[i])
    sorted_chars = sorted(chars.values())
    return chr(sorted_chars[3])
