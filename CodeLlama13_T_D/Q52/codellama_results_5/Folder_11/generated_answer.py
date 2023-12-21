
def palindrome_of_length_n(s):
    return set([p for p in re.findall('[a-zA-Z]{77}', s) if p == p[::-1]])
