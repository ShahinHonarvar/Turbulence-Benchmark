
def return_nth_smallest_ascii(s):
    s_substring = s[0:18]
    sorted_substring = sorted(s_substring)
    return sorted_substring[17]
