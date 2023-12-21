 
def filter_chars(string):
    return string[:15] + string[15:56].replace('W', '').replace('X', '').replace('Y', '').replace('Z', '') + string[56:]
