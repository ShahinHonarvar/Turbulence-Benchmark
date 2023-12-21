
def return_nth_smallest_ascii(input_str):
    selected_chars = sorted([ch for ch in set(input_str[1:32])])
    return selected_chars[5]
