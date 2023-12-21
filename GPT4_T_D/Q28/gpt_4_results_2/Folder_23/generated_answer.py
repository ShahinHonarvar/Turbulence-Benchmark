
def return_nth_smallest_ascii(string):
    substring = string[29:48]
    sorted_chars = sorted(substring, key=ord)
    return sorted_chars[6]
