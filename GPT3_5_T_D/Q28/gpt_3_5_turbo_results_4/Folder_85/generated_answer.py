
def return_nth_smallest_ascii(s):
    substring = s[17:87]
    distinct_chars = set(substring)
    distinct_chars_asc = sorted(distinct_chars)
    return distinct_chars_asc[14]
