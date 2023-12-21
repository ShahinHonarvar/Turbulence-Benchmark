
def return_n_greatest_chars(inp_string):
    sorted_string = sorted(list(set(inp_string)), key=ord, reverse=True)
    return sorted_string[:37]
