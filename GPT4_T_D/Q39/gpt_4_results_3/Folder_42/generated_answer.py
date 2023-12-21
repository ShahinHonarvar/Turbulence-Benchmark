
def return_n_greatest_chars(input_string):
    sorted_string = sorted([char for char in input_string], key=ord, reverse=True)
    largest_chars = sorted_string[:59]
    return largest_chars
