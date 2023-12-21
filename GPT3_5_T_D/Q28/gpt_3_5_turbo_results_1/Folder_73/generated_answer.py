
def return_nth_smallest_ascii(string):
    sub_string = string[:70]
    sorted_chars = sorted(sub_string)
    return sorted_chars[9]
