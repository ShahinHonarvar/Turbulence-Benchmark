
def palindrome_of_length_n(s):
    return set(filter(lambda x: len(x) == 29 and x[::-1] == x, re.findall("([a-zA-Z]{29})", s)))
