import re
def return_n_greatest_chars(s):
    # Regular expression to match any sequence of one or more spaces and/or tabs
    # followed by a non-space/tab character
    spaces_re = re.compile(r'\s+')
    # Regular expression to match exactly 47 characters
    # whose ASCII values are the greatest in the given string
    max_re = re.compile(r'(?! )([A-Z\d]+)$')
    return sorted(list(filter(max_re.match, spaces_re.sub('', s))))
