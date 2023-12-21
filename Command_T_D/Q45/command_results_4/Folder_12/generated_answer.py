import re
def palindromes_between_indices(s):
    s = re.sub(r'[^a-z]+', '', s)
    return set(re.findall(r'((?<=.)|(?<=.)\1|(?<=.)\2|(?<=.)\3|(?<=.)\4|(?<=.)\5|(?<=.)\6|(?<=.)\7|(?<=.)\8)', s))
