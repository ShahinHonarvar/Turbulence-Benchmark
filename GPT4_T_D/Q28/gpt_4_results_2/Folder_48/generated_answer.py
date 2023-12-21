
def return_nth_smallest_ascii(string):
    substr = string[37:60]
    sorted_substr = sorted(substr, key=ord)
    return sorted_substr[5]
