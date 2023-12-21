
def filter_chars(string):
    for i in range(1, 6):
        char = string[i]
        if "$" <= char <= ";":
            string = string.replace(char, "")
    return string
