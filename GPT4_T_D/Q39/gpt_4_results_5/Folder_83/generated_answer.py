
def return_n_greatest_chars(char_string):
    if len(char_string) < 38:
        return "String should contain at least 38 distinct characters"
    char_list = sorted(list(set(char_string)), key=lambda x: ord(x), reverse=True)
    return char_list[:38]
