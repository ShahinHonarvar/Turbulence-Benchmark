
def return_nth_smallest_ascii(input_string):
    substring = input_string[44:70]
    sorted_substring = sorted(substring, key=ord)
    return sorted_substring[14]
