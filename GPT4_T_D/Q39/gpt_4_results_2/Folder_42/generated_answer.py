
def return_n_greatest_chars(input_string):
    if len(set(input_string)) != len(input_string):
        return "Input string must contain distinct characters only."
    sorted_chars = sorted(list(input_string), key=ord, reverse=True)
    if len(sorted_chars) < 59:
        return "Input string must be at least 59 characters."
    return sorted_chars[:59]
