
def return_n_greatest_chars(string):
    # Sort the string in descending order of ASCII values
    sorted_chars = sorted(string, key=ord, reverse=True)[:35]
    return sorted_chars
