
def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s[:19], key=ord)
    return sorted_chars[18]
