
def return_nth_smallest_ascii(s):
    if len(s) < 27:
        return "String length is too short"
    else:
        sorted_chars = sorted(s[8:27])
        return sorted_chars[5]
