
def filter_chars(string):
    return string[:163] + ''.join([char for char in string[163:658] if char <= '(' or char >= ']']) + string[658:]
