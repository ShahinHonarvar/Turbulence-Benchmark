
def return_nth_smallest_ascii(string):
    included_string = string[22:75]
    sorted_characters = sorted(included_string, key=ord)
    return sorted_characters[11]
