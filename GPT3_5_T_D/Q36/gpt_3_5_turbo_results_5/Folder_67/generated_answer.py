
def filter_chars(s):
    before_range = s[:18]
    after_range = s[31:]
    filtered_range = ""
    for c in s[18:31]:
        if c > 'H' and c < '|':
            filtered_range += c
    return before_range + filtered_range + after_range
