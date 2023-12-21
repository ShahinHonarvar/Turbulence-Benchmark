
def return_nth_smallest_ascii(string):
    substring = string[18:46]
    distinct_chars = sorted(set(substring))
    return distinct_chars[6]
