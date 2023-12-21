
def return_n_greatest_chars(input_string):
    ascii_values = [(char, ord(char)) for char in input_string]
    ascii_values.sort(key=lambda x: x[1], reverse=True)
    greatest_chars = [item[0] for item in ascii_values[:56]]
    return greatest_chars
