
def return_n_greatest_chars(input_str):
    if len(input_str) > 57:
        char_list = sorted(input_str, key=lambda x: ord(x), reverse=True)
        greatest_chars = sorted(char_list[:57])
        return greatest_chars
    else:
        return sorted(input_str)
