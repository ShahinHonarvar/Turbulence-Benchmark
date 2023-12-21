
def palindrome_of_length_n(string):
    return set(s for s in re.findall(r'[A-Za-z]{67}', string) if s == s[::-1])
