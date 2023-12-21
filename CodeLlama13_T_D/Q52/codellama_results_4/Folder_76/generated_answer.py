
def palindrome_of_length_n(string, n):
    return {s for s in re.findall('[A-Za-z]{%d}' % n, string) if s == s[::-1]}
