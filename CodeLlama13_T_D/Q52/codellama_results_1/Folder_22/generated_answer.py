
def palindrome_of_length_n(string):
    return set(s for s in re.findall(r'[a-zA-Z]{20}', string) if s == s[::-1])
