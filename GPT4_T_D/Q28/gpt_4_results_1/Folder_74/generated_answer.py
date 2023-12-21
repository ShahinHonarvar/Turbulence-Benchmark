
def return_nth_smallest_ascii(s):
    sub_string = s[1:32]
    sorted_chars = sorted(sub_string)
    return sorted_chars[5]
