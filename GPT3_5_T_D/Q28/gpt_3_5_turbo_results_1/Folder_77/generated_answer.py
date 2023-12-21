
def return_nth_smallest_ascii(string):
    substring = string[63:77]
    distinct_chars = list(set(substring))
    distinct_chars.sort()
    return distinct_chars[13]
