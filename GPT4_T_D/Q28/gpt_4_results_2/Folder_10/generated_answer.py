
def return_nth_smallest_ascii(string):
    substring = string[38:83]
    sorted_chars = sorted(substring, key=ord)
    return sorted_chars[19]
