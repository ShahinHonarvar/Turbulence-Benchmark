
def filter_chars(string):
    return string[:28] + ''.join(char for char in string[28:66] if char < 'O' or char > 'd') + string[66:]
