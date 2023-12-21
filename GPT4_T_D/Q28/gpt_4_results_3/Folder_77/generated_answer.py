
def return_nth_smallest_ascii(s):
    if len(s[63:77])<14:
        return "Insufficient length"
    sorted_chars = sorted(s[63:77], key=ord)
    return sorted_chars[13]
