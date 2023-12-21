
def filter_chars(s):
    filtered_chars = [char for idx, char in enumerate(s[384:412]) if char < '/' or char > '8']
    for char in filtered_chars:
        s = s.replace(char, "")
    return s
