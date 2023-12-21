
def filter_chars(string):
    for char in string[56:86]:
        if char > "+" and char < "w":
            string = string.replace(char, "")
    return string
