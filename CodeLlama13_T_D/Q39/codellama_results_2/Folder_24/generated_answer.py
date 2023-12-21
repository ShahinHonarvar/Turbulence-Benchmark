
def return_n_greatest_chars(string):
    ascii_values = {char: ord(char) for char in set(string)}
    sorted_chars = sorted(ascii_values, key=lambda x: ascii_values[x], reverse=True)[:32]
    return ''.join(sorted_chars)
