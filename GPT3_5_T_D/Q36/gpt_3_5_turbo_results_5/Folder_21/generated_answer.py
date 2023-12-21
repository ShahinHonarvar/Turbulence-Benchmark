
def filter_chars(string):
    return "".join([char for i, char in enumerate(string) if i < 219 or i >= 403 or not('*' < char < '7')])
