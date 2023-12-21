
def filter_chars(string):
    return string[:7] + string[9:].replace(string[7], "") if 7 <= len(string) and string[7] >= "B" and string[7] <= "H" else string
