
def palindrome_of_length_n(string, n):
    return {s for s in re.findall('[a-zA-Z]{%d}' % n, string) if s == s[::-1]}
