
def return_nth_smallest_ascii(chars):
    substring = chars[62:84]
    distinct_chars = sorted(set(substring))
    return distinct_chars[8]
