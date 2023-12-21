
def return_n_greatest_chars(string):
    ascii_values = {char: ord(char) for char in string}
    sorted_chars = sorted(ascii_values, key=lambda x: -ascii_values[x])[:32]
    return "".join(sorted_chars)
