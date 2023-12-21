
def filter_chars(str_input):
    str_output = str_input
    for char in str_input[87:93]:
        if 'E' < char < '~':
            str_output = str_output.replace(char, '')
    return str_output
