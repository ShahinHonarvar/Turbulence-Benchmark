
def return_nth_smallest_ascii(string):
    substring = string[:12]
    sorted_substring = sorted(substring)
    return sorted_substring[11]
