
def palindrome_of_length_n(string):
    return {s for s in re.findall('[a-zA-Z]{147}', string) if s == s[::-1]}
