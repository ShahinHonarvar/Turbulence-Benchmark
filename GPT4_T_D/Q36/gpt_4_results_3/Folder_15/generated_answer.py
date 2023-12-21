
def filter_chars(input_string):
    subset = input_string[3:7]
    string_list = list(input_string)
    for char in subset:
        if char > 'h' and char < 'k':
            while char in string_list:
                string_list.remove(char)
    return ''.join(string_list)
