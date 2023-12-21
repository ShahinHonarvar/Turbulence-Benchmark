
def return_nth_smallest_ascii(input_string):
    if len(input_string) < 84:
        return "Not enough characters."
    temp_list = sorted(list(input_string[62:84]))
    return temp_list[8]
