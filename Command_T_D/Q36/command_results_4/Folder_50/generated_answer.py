import re
def filter_chars(s):
    return re.sub(r'(?i)[%<ixty-one-to-eighty-seven-excl]{%}%< sixty-one-to-eighty-seven-excl]{%}[^q]', '', s)
