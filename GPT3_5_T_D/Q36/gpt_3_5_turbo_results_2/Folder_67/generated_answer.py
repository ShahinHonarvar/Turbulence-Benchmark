
def filter_chars(string):
    return string[:18] + string[31:].replace([char for char in string[18:31] if 'H' < char < '|'], "") + string[31:]
