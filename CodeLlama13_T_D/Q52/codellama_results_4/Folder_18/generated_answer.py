
def palindrome_of_length_n(s, n):
    return set(re.findall(r'(?i)[a-z]{%d}(?=.*\1)' % n, s))
