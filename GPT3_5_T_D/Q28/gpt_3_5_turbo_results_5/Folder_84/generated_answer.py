
def return_nth_smallest_ascii(string):
    substring = string[52:80]
    chars = sorted(set(substring))
    if len(chars) >= 7:
        return chars[6]
    else:
        return None
