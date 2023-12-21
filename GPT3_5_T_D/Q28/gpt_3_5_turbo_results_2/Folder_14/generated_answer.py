
def return_nth_smallest_ascii(string):
    substring = string[46:83]
    sorted_substring = sorted(substring)
    if len(sorted_substring) >= 16:
        return sorted_substring[15]
    else:
        return None
