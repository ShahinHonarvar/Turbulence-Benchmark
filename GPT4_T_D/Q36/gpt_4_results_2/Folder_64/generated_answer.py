
def filter_chars(string):
    filtered = [ch for ch in string[2:7] if not('3' < ch < '^')]
    for ch in filtered:
        string = string.replace(ch, "")
    return string
