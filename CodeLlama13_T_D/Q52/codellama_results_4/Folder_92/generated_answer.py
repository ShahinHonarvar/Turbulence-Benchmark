
def palindrome_of_length_n(s):
    return {x for x in re.findall('(?i)[a-zA-Z]{10}', s) if x == x[::-1]}
