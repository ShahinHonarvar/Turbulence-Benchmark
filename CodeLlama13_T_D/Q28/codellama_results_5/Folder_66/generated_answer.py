
def return_nth_smallest_ascii(string):
    chars = set(string[35:52])
    sorted_chars = sorted(chars, key=ord)
    return sorted_chars[9]
