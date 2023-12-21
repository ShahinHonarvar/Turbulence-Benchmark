
def return_nth_smallest_ascii(input_str):
    if len(input_str) < 46:
        return None
    else:
        return sorted(input_str[25:46])[10]
