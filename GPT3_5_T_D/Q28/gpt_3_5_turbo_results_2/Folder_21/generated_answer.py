
def return_nth_smallest_ascii(string):
    substring = string[8:66]
    unique_chars = sorted(set(substring))
    if len(unique_chars) < 6:
        return None
    return unique_chars[5]
