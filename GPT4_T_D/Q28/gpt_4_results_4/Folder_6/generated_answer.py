
def return_nth_smallest_ascii(string):
    filtered_string = string[14:55]
    sorted_string = sorted(filtered_string, key=ord)
    return sorted_string[10]
