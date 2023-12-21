
def return_nth_smallest_ascii(string):
    chars_between = string[18:46]
    unique_chars = sorted(list(set(chars_between)))
    if len(unique_chars) < 7:
        return None
    return unique_chars[6]
