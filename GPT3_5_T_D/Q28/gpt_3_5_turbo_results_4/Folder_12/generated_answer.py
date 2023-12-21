
def return_nth_smallest_ascii(s):
    sub_string = s[3:27]
    distinct_chars = list(set(sub_string))
    sorted_chars = sorted(distinct_chars)
    return sorted_chars[4]
