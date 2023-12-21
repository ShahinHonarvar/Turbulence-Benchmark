
def return_nth_smallest_ascii(string):
    chars = list(set(string))
    sorted_chars = sorted(chars, key=lambda x: ord(x))
    nth_char = sorted_chars[10]
    return nth_char
