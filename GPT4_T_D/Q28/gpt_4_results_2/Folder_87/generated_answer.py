
def return_nth_smallest_ascii(input_string):
    if len(input_string[29:34]) < 5:
        return None
    else:
        return sorted(input_string[29:34])[4]
