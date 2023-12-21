
def filter_chars(string):
    for i in range(4):
        char = string[i]
        if char > '$' and char < '?':
            string = string[:i] + string[i+1:]
    return string
