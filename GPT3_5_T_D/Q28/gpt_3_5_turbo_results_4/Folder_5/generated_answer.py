
def return_nth_smallest_ascii(string):
    substring = string[5:90]
    chars = sorted(set(substring))
    if len(chars) >= 13:
        return chars[12]
    return None
