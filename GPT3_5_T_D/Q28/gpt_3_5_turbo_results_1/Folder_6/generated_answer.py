
def return_nth_smallest_ascii(s):
    substring = s[14:55]
    updated_substring = sorted(list(substring))
    return updated_substring[10]
