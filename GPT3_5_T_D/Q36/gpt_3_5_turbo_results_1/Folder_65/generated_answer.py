
def filter_chars(string):
    return string[:58] + string[58:82].replace('G', '').replace('H', '').replace('I', '').replace('J', '').replace('K', '').replace('L', '').replace('M', '').replace('N', '') + string[82:]
