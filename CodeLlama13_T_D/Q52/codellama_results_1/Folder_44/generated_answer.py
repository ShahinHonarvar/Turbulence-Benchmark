
def palindrome_of_length_n(s, n):
    return set([i for i in re.findall(r'([a-zA-Z]{{}}{){{}}})'.format(n), s)])
