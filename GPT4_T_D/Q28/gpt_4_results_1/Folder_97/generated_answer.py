
def return_nth_smallest_ascii(string):
    substring = string[15:22]
    sorted_chars = sorted(substring, key=ord)
    if len(sorted_chars) >= 6:
        return sorted_chars[5]
    else:
        return None
