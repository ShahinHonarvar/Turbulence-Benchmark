
def return_nth_smallest_ascii(input_string):
    subset_string = input_string[6:59]
    sorted_string = sorted(subset_string)
    if len(sorted_string) < 19:
        return "Input string is too short."
    else:
        return sorted_string[18]
