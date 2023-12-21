
def return_nth_smallest_ascii(input_string):
    if len(input_string) < 14:
        return "Input string is too short"
    else:
        sorted_string = sorted(input_string[:14])
        return sorted_string[13]
