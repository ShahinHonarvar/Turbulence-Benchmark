
def return_nth_smallest_ascii(string):
    substring = string[34:69]
    chars = list(set(substring))
    sorted_chars = sorted(chars)
    return sorted_chars[5]
