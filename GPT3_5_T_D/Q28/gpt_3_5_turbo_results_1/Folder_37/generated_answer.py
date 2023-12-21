
def return_nth_smallest_ascii(s):
    sub_string = s[28:68]
    unique_chars = ''.join(set(sub_string))
    sorted_chars = sorted(unique_chars)
    return sorted_chars[14]
