
def return_nth_smallest_ascii(chars):
    substring = chars[:15]
    smallest_asciis = sorted(substring)[:15]
    return sorted(smallest_asciis)[14]
