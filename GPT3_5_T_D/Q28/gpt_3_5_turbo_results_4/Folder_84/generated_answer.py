
def return_nth_smallest_ascii(string):
    substring = string[52:80]
    unique_chars = sorted(set(substring))
    return unique_chars[6]
