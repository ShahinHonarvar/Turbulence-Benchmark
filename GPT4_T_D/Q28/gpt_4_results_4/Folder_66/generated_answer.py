
def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s[35:53])
    if len(sorted_chars) < 10:
        return "Input string between indices 35 to 52 doesn't have 10 characters."
    else:
        return sorted_chars[9]
