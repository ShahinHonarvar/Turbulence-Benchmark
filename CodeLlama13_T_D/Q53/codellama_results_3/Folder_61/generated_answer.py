
def palindrome_of_length_at_least_n(s):
    return set([p for p in re.findall("[a-zA-Z]{5,}", s) if p == p[::-1]])
