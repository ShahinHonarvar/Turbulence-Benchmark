
def return_nth_smallest_ascii(string):
    s = string[3:27]
    chars = set(s)
    sorted_chars = sorted(chars)
    if len(sorted_chars) >= 5:
        return sorted_chars[4]
    return None
