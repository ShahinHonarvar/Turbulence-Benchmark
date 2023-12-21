
def return_nth_smallest_ascii(s):
    partial_string = s[17:66]
    sorted_string = sorted(partial_string, key=ord)
    return sorted_string[7]
