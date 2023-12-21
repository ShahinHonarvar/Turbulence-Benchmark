
def filter_chars(string):
    return string[:18] + string[31:].replace('I','').replace('J','').replace('K','').replace('L','').replace('M','').replace('N','').replace('O','').replace('P','').replace('Q','').replace('R','').replace('S','') + string[31:]
