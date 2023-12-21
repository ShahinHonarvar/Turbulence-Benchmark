
def palindrome_of_length_n(s):
    n = 85
    return {x for x in re.findall(r'([a-z]{%d})|([a-z]{%d})' % (n, n), s) if x == x[::-1]}
