
def return_n_greatest_chars(input_str):
    if len(input_str) < 39:
        return "Error: Not enough distinct characters!"
    else:
        sorted_list = sorted(input_str, key=ord, reverse=True)
        return sorted_list[:39]
