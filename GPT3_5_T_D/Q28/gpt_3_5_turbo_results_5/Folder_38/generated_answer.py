
def return_nth_smallest_ascii(string):
    substring = string[:46]
    chars = sorted(set(substring))
    return chars[9]
