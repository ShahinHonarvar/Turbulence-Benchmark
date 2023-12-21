
def filter_chars(string):
    return string[:503] + ''.join([c for c in string[503:754] if not ('9' <= c <= 'w')]) + string[754:]
