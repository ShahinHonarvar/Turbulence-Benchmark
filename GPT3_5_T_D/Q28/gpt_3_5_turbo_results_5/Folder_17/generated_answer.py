
def return_nth_smallest_ascii(string):
    substring = string[3:34]
    distinct_chars = ''.join(set(substring))
    sorted_chars = sorted(distinct_chars)
    return sorted_chars[3]
