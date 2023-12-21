
def return_nth_smallest_ascii(s):
    first_18_chars = s[:18]
    sorted_chars = sorted(first_18_chars)
    return sorted_chars[17]
