
def return_nth_smallest_ascii(s):
    substring = s[22:75]
    sorted_substring = sorted(substring, key=ord)
    return sorted_substring[11]
