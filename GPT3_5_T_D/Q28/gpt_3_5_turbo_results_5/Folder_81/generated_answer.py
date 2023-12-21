
def return_nth_smallest_ascii(string):
    sub_string = string[:14]
    sorted_chars = sorted(sub_string)
    return sorted_chars[13]
