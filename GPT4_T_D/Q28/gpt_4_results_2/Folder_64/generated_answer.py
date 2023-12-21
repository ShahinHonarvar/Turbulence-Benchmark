
def return_nth_smallest_ascii(s):
    if len(s) < 7:
        return "String length less than 7"
    else:
        sorted_chars = sorted(s[0:7])
        return sorted_chars[6]
