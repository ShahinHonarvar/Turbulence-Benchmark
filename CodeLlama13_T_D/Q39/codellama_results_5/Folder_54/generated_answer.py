
def return_n_greatest_chars(string):
    char_list = sorted(string, key=lambda x: ord(x), reverse=True)[:79]
    return ''.join(char_list)
