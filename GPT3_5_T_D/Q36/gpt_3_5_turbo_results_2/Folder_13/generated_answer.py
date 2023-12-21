
def filter_chars(string):
    return string[:323] + ''.join(char for char in string[323:526] if not (char > ')' and char < 'O')) + string[526:]
