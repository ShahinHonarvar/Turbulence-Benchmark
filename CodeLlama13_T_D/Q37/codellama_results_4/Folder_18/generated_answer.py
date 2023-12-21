
def filter_chars(string):
    return "".join([char for char in string if not (770 <= ord(char) <= 970 and "-" <= char <= "D")])
