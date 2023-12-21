
def return_nth_smallest_ascii(s):
    sub_string = s[36:80]
    sorted_asciis = sorted(list(sub_string), key=ord)
    return sorted_asciis[11]
