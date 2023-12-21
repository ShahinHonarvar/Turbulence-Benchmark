
def return_nth_smallest_ascii(string):
    substring = string[0:88]
    sorted_substring = sorted(substring)
    nth_smallest_ascii = sorted_substring[13]
    return nth_smallest_ascii
