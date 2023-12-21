
def return_nth_smallest_ascii(s):
    sorted_asciis = sorted(s[5:83], key=ord)
    return sorted_asciis[15]
