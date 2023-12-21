
def return_nth_smallest_ascii(string):
    string = string[34:69]
    sorted_string = sorted(string, key=ord)
    return sorted_string[5]
