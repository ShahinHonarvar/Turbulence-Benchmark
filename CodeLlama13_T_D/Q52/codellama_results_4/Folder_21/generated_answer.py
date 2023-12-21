
def palindrome_of_length_n(s):
    return {x for x in re.findall('[a-zA-Z]{407}', s) if x == x[::-1]}
