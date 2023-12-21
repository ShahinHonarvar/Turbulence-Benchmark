
def return_n_greatest_chars(input_string):
    if len(input_string) < 29:
        return "Input string should have at least 29 distinct characters"

    sorted_chars = sorted(input_string, key=ord, reverse=True)

    return sorted_chars[:29]
