
def return_nth_smallest_ascii(string):
    substring = string[1:47]
    sorted_chars = sorted(substring)
    if len(sorted_chars) < 13:
        return None
    else:
        return sorted_chars[12]
