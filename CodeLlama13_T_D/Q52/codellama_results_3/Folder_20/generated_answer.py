
def palindrome_of_length_n(string, n):
    return {s[::-1].lower() for s in re.findall('.{' + str(n) + '}', string) if s[::-1].lower() == s.lower()}
