
def return_n_smallest_chars(input_string):
    if len(input_string) < 48:
        return "The input string should have at least 48 distinct characters"
    else:
        sorted_string = sorted(input_string)
        output = sorted_string[:48]
        return output
