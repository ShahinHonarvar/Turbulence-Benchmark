
def return_nth_smallest_ascii(chars):
    substring = chars[63:77]
    sorted_chars = sorted(substring, key=lambda x: ord(x))
    return sorted_chars[13]
