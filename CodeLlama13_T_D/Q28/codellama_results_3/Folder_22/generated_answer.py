
def return_nth_smallest_ascii(string):
    chars = set(string)
    ascii_vals = {char: ord(char) for char in chars}
    sorted_chars = sorted(ascii_vals, key=ascii_vals.get)
    return sorted_chars[16]
