
def return_nth_smallest_ascii(s):
    substring = s[25:46]
    sorted_substring = sorted(substring, key=lambda x: ord(x))
    return sorted_substring[10]
