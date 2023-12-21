
def return_nth_smallest_ascii(s):
    substring = s[40:61]
    sorted_chars = sorted(substring, key=ord)
    if len(sorted_chars) >= 19:
        return sorted_chars[18]
    else:
        return None
