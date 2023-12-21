
def return_nth_smallest_ascii(string):
    substring = string[58:86]
    sorted_substring = sorted(substring, key=lambda x: ord(x))
    return sorted_substring[18]
