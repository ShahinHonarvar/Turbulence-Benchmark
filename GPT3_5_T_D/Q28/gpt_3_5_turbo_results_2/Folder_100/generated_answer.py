
def return_nth_smallest_ascii(string):
    substr = string[5:48]
    chars = set(substr)
    sorted_chars = sorted(chars)
    return sorted_chars[12]
