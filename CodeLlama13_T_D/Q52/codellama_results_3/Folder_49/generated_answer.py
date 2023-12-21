
def palindrome_of_length_n(s):
    return set([x for x in re.findall("[A-Za-z]{47}", s) if x == x[::-1]])
