
def palindrome_of_length_n(s):
    return {x for x in re.findall('(?i)([A-Za-z]{100})', s) if x == x[::-1]}
