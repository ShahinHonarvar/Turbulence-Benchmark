
def return_nth_smallest_ascii(string):
    substring = string[51:61]
    distinct_chars = sorted(set(substring))
    return distinct_chars[4]
