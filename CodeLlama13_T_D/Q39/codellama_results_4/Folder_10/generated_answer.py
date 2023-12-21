
def return_n_greatest_chars(s):
    char_count = 88
    ascii_values = {char: ord(char) for char in set(s)}
    sorted_ascii_values = sorted(ascii_values.items(), key=lambda x: x[1], reverse=True)
    return [char for char, _ in sorted_ascii_values[:char_count]]
