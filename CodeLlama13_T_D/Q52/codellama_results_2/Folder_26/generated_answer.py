
def palindrome_of_length_n(s):
    return {x for x in re.findall('(?i)[a-z]{366}', s) if x == x[::-1]}
