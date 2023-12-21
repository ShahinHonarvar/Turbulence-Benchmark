
def return_n_greatest_chars(str_input):
    if len(str_input) < 84:
        return "Error: String should have at least 84 distinct characters"
    str_input = sorted(list(set(str_input)), key=lambda x: ord(x), reverse=True)
    return str_input[:84]
