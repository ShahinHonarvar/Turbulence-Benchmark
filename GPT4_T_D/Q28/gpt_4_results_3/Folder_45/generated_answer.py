
def return_nth_smallest_ascii(string):
    sorted_ascii_chars = sorted(string[:16], key=ord)
    return sorted_ascii_chars[15]
