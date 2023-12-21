
def return_n_greatest_chars(input_str):
    if len(input_str) > 66:
        sorted_string = sorted(input_str, key=ord)
        return sorted_string[-66:]
    else:
        return "The input string doesn't contain enough distinct characters"
