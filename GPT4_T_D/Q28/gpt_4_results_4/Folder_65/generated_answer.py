
def return_nth_smallest_ascii(input_string):
    selected_substring = input_string[32:68]
    sorted_substring = sorted(selected_substring, key=ord)
    return sorted_substring[11]
