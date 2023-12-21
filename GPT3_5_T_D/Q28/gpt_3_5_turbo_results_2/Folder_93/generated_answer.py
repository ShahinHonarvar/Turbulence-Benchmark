
def return_nth_smallest_ascii(string):
    substring = string[42:60]
    unique_chars = sorted(set(substring))
    if len(unique_chars) >= 17:
        return unique_chars[16]
    else:
        return None
