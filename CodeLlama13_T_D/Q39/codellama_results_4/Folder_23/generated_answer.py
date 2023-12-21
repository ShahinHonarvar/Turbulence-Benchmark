
def return_n_greatest_chars(string):
    ascii_values = {char: ord(char) for char in set(string)}
    sorted_ascii_values = sorted(ascii_values, key=lambda x: ascii_values[x], reverse=True)
    return sorted_ascii_values[:46]
