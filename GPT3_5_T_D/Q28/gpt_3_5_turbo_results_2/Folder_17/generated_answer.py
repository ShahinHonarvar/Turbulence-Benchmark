
def return_nth_smallest_ascii(string):
    substring = string[3:34]
    distinct_chars = sorted(set(substring))
    return distinct_chars[3]
