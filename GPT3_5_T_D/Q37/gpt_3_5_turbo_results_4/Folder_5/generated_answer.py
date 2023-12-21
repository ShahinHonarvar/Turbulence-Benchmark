
def filter_chars(string):
    string = list(string)
    for i in range(24, 83):
        if '5' <= string[i] <= '<':
            string = [c for c in string if c != string[i]]
    return ''.join(string)
