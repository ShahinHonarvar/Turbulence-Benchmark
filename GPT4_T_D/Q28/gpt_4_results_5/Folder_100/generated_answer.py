
def return_nth_smallest_ascii(input_string):
    substring = input_string[5:48]
    return sorted(substring, key=ord)[12]
