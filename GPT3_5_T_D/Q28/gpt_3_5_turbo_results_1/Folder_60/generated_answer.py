
def return_nth_smallest_ascii(string):
    sub_string = string[36:80]
    sub_string = ''.join(sorted(sub_string))
    return sub_string[11]
