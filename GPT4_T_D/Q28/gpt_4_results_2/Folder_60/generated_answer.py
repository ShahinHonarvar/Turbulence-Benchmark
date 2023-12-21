
def return_nth_smallest_ascii(string):
    substring = string[36:80]
    sorted_substring = sorted(substring, key=ord)
    return sorted_substring[11]
