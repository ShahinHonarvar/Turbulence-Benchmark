
def return_nth_smallest_ascii(string):
    substring = string[0:70]
    sorted_chars = sorted(set(substring))
    if len(sorted_chars) >= 10:
        return sorted_chars[9]
    else:
        return None
