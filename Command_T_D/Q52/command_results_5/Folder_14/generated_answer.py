import re
def palindrome_of_length_n(s):
    return {m.group() for m in re.finditer(r'([a-z]+)(?=\1)', s)}
