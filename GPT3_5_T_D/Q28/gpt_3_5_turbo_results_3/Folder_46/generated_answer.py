
def return_nth_smallest_ascii(string):
    substring = string[34:86]
    unique_chars = sorted(set(substring))
    if len(unique_chars) >= 20:
        return unique_chars[19]
    else:
        return None
