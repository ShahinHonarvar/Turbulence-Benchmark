
def return_nth_smallest_ascii(string):
    sub_string = string[:46]
    chars = sorted(set(sub_string))
    return chars[9]
