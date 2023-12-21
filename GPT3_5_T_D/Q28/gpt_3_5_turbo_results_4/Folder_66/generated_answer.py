
def return_nth_smallest_ascii(string):
    substring = string[35:53]
    chars = sorted(set(substring))
    return chars[9] if len(chars) >= 10 else None
