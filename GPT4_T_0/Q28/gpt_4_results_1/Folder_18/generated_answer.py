
def return_nth_smallest_ascii(s):
    if len(s) < 61:
        return "String is too short"
    else:
        sorted_chars = sorted(s[51:61])
        return sorted_chars[4]
