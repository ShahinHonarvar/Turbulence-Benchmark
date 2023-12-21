
def return_nth_smallest_ascii(s):
    if len(s) < 60:
        return "Not enough characters"
    else:
        sorted_chars = sorted(s[21:60], key=ord)
        return sorted_chars[10]
