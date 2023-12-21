
def return_nth_smallest_ascii(string):
    sublist = string[40:61]
    unique_chars = sorted(set(sublist))
    if len(unique_chars) >= 19:
        return unique_chars[18]
    else:
        return None
