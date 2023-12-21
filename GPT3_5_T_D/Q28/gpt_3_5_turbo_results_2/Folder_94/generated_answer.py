
def return_nth_smallest_ascii(string):
    substring = string[6:59]
    substring = ''.join(sorted(substring))
    return substring[18]
