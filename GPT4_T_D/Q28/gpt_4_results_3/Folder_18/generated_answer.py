
def return_nth_smallest_ascii(input_string):
    substr = input_string[51:61]
    sorted_substr = sorted(substr, key=ord)
    return sorted_substr[4]
