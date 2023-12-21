
def return_nth_smallest_ascii(s):
    sub_string = s[20:81]
    unique_chars = sorted(set(sub_string))
    return unique_chars[10]
